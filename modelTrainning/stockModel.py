'''
convert input event to (O1, P, O2, O1+P, P+O2, O1+P+O2) the previous day, the day a week before, the day a month before
output:
'''
import tensorflow as tf
import numpy as np
import gensim
import pickle
import datetime
import pandas as pd
from sklearn.cross_validation import train_test_split

# model = gensim.models.Word2Vec.load_word2vec_format(r'E:\stuff\tmp\model\extracReuters_modelvec', binary=False)
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
def changeEventSet():
    event_dataset = {}
    for i in range(len(eventWord_time)):
        try:
            vec_actor = getWordVec(eventWord_time[i]["subWord"])
            vec_action = getWordVec(eventWord_time[i]["eventWord"])
            vec_object = getWordVec(eventWord_time[i]["objWord"])
            event_time = datetime.datetime.strptime(eventWord_time[i]["time"], "%Y%m%d").date()
            vec_com1 = getWordVec(eventWord_time[i]["subWord"] + eventWord_time[i]["eventWord"])
            vec_com2 = getWordVec(eventWord_time[i]["eventWord"] + eventWord_time[i]["objWord"])
            vec_com3 = getWordVec(
                eventWord_time[i]["subWord"] + eventWord_time[i]["eventWord"] + eventWord_time[i]["objWord"])
            tmp = np.vstack((vec_actor, vec_action, vec_object, vec_com1, vec_com2, vec_com3))
            event_dataset[event_time] = np.reshape(tmp, [600])
        except Exception as e:
            print(e, eventWord_time[i])
    return event_dataset

# get dataset time: [600*3], up
def getDataSet(period):
    dataSet = []
    # stock_info = pickle.load(open("stock_info_next"+str(period)+".txt", "rb"))
    stock_info = pickle.load(open("./traindata/stock_info.pkl", "rb"))

    event_dataset = changeEventSet()
    beginTime = datetime.date(2006, 11, 21)
    endTime = datetime.date(2013, 11, 20)
    aTime = datetime.timedelta(days=-period)
    cnt = 0
    while beginTime != endTime:
        if ((beginTime) in event_dataset):
            today = event_dataset[beginTime]
            tmp = today
            if not stock_info[beginTime.strftime("%Y-%m-%d")].empty:
                tmp = np.hstack((tmp, stock_info[beginTime.strftime("%Y-%m-%d")]["label"]))
                dataSet.append(tmp)
        beginTime = beginTime + datetime.timedelta(days=1)
        cnt += 1
        if cnt % 100 == 0:
            print("============================", beginTime, endTime)
    print("===================done getdataset")
    return np.array(dataSet)


# def layer
def add_layer(inputs, in_size, out_size, layer_name, activation_function=None, ):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, )
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


def compute_accuracy(v_xs, v_ys):
    global y3
    y_pre = sess.run(y3, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result


# define placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None, 600])  # 600
ys = tf.placeholder(tf.float32)

# create tensorflow structure
y1 = add_layer(xs, 600, 256, 'l1', activation_function=tf.nn.sigmoid)
y2 = add_layer(y1, 256, 64, 'l2', activation_function=tf.nn.sigmoid)
y3 = add_layer(y2, 64, 1, 'l3', activation_function=tf.nn.sigmoid)

# the loss between prediction and real data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(y3), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)

# train dataset and test dataset
dataSet = getDataSet(1)
dataSet = pd.DataFrame(dataSet).dropna()
dataSet.dtype = 'float32'
dataSet = np.array(dataSet)

X, y = dataSet[:,:-1], dataSet[:,-1]
X = np.reshape(X,[-1,600])
y = np.reshape(y, [-1,1])
print(X.shape, y.shape)

# Add ops to save and restore all the variables
saver = tf.train.Saver()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print("====================begin train================================")
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(3000):
    _, lossvalue = sess.run([train_step,cross_entropy], feed_dict={xs: X_train, ys: y_train})
    if i % 50 == 0:
        print("========================", i)
        print(lossvalue)
        # print(compute_accuracy(X_test, y_test))

y_pre = sess.run(y3, feed_dict={xs: X_test})
cnt, count = 0, 0
for i in range(len(y_pre)):
    if y_test[i] == -1:
        continue
    else:
        count += 1
    if y_pre[i]<0.5:
        y_pre[i] = 0
    if y_pre[i]>=0.5:
        y_pre[i] = 1
    if y_pre[i] == y_test[i]:
        cnt += 1

print(cnt/count)
# print(y_test)
# print(y_pre)

# Save the variables to disk
save_path = saver.save(sess, "./model/stockModel.ckpt")

print("Event Model saved in file: ", save_path)

def caculateMCC(y, pre):
    tp, fp, fn, tn = 0,0,0,0
    for i in range(len(y)):
        if y_test[i] == -1:
            continue
        if y[i]==1 and pre[i]==1:
            tp += 1
        elif y[i]==1 and pre[i]==0:
            fn += 1
        elif y[i]==0 and pre[i]==1:
            fp += 1
        elif y[i]==0 and pre[i]==0:
            tn += 1
    import math
    print(tp, fp, fn, tn)
    mcc = (tp*tn-fp*fn)*1.0 / (math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)))
    return mcc

print(caculateMCC(y_test, y_pre))