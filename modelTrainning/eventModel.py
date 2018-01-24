'''
use tensorflow for event embedding
input n_size*[[actor],[action],[object]]
output event embedding & model
'''

import tensorflow as tf
import pickle
import numpy as np
import datetime
import pandas as pd

wordsDic = pickle.load(open("./traindata/wordsDic.pkl", "rb"))
eventWord_time = pickle.load(open("./traindata/eventWord_time.pkl", "rb"))


def getWordVec(str):
    word = str.split()
    if len(word) == 1:
        if str in wordsDic:
            return np.array(wordsDic[str])
        else:
            return np.zeros([1, 100])
    else:
        vec = np.zeros([1, 100])
        cnt = 0
        for w in word:
            if w in wordsDic:
                vec += np.array(wordsDic[w]).reshape([1, 100])
                cnt += 1
            else:
                continue
        return np.divide(vec, cnt).reshape([-1, 100])


# change eventset to time: [600]
def getEventSet():
    event_dataset = []
    event_time_set = []
    for i in range(len(eventWord_time)):
        try:
            vec_actor = getWordVec(eventWord_time[i]["subWord"])
            vec_action = getWordVec(eventWord_time[i]["eventWord"])
            vec_object = getWordVec(eventWord_time[i]["objWord"])
            event_time = datetime.datetime.strptime(eventWord_time[i]["time"], "%Y%m%d").date()
            tmp = np.vstack((vec_actor, vec_action, vec_object))
            if event_time < datetime.date(2010, 11, 20):
                event_dataset.append(tmp)
                event_time_set.append(event_time)
        except Exception as e:
            print(e, eventWord_time[i])
    return event_time_set, np.array(event_dataset)


# Parameters
dimension = 100
learning_rate = 1e-10
training_epochs = 100  # 500
k = 64
batch_size = 256

# input
event = tf.placeholder(tf.float32, [None, dimension * 3])
event_corrupted = tf.placeholder(tf.float32, [None, dimension * 3])

# define variables
tensor = {
    't1': tf.Variable(tf.random_normal([dimension, k])),
    't2': tf.Variable(tf.random_normal([dimension, k])),
    't3': tf.Variable(tf.random_normal([k, k]))
}

weights = {
    'w1': tf.Variable(tf.zeros([dimension * 2, k]) + 0.1),
    'w2': tf.Variable(tf.random_normal([dimension * 2, k])),
    'w3': tf.Variable(tf.random_normal([k * 2, k]))
}

baises = {
    'b1': tf.Variable(tf.zeros([1, k]) + 0.1),
    'b2': tf.Variable(tf.zeros([1, k]) + 0.1),
    'b3': tf.Variable(tf.zeros([1, k]) + 0.1)
}


# define NTN
def tnn(event):
    actor = event[:, :dimension]
    action = event[:, dimension:-dimension]
    object = event[:, -dimension:]

    r1 = tf.matmul(tf.reshape(tf.stack([actor, action]), [-1, 2 * dimension]), weights['w1']) + \
         baises['b1']

    r2 = tf.matmul(tf.reshape(tf.stack([action, object]), [-1, 2 * dimension]), weights['w2']) + \
         baises['b2']
    u = tf.matmul(tf.reshape(tf.stack([r1, r2]), [-1, 2 * k]), weights['w3']) + \
        baises['b3']

    u = tf.Print(u, [u], message="This is u: ")

    print('===done=======')
    return u


pred = tnn(event)
corrupted_pred = tnn(event)

loss = -tf.reduce_sum(pred * tf.log(tf.clip_by_value(corrupted_pred, 1e-1, 1.0)), reduction_indices=[1])
# loss = tf.maximum(tf.zeros([64, 64]), tf.ones([64, 64]) - pred + corrupted_pred)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

# load dataSet
eTime, eSet = getEventSet()
input_event = np.reshape(eSet, [-1, 3 * dimension])
input_event = pd.DataFrame(input_event).fillna(0)
input_event.dtype = 'float32'
input_event = np.array(input_event)

# Add ops to save and restore all the variables
saver = tf.train.Saver()

print("====================begin train================================")
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(200):
    _, lossvalue = sess.run([optimizer, loss], feed_dict={event: input_event})
    test_pre = sess.run(pred, feed_dict={event: input_event})
    # print(test_pre)
    print(lossvalue)

test_pre = sess.run(pred, feed_dict={event: input_event})

# Save the variables to disk
save_path = saver.save(sess, "./model/eventModel.ckpt")

print("Event Model saved in file: ", save_path)

result = list(zip(eTime, test_pre))
# print(result[:2])
pickle.dump(result, open("./traindata/eventEmbedding01.pkl", "wb"), True)
