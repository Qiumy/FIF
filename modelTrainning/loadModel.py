import tensorflow as tf
import pickle
import numpy as np
import datetime
import pandas as pd


def loadEventModel(eventEmbedding):
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

    sess = tf.Session()

    saver = tf.train.Saver()

    # restore model
    saver.restore(sess, "./model/eventModel.ckpt")
    print("restore model sucesss")

    # load dataSet

    test_pre = sess.run(pred, feed_dict={event: eventEmbedding})
    print(test_pre)
    return test_pre


# ==============================predict model begin====================================
def loadStockModel(inputEvent):
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

    # define placeholder for inputs to network
    xs = tf.placeholder(tf.float32, [None, 600])  # 600

    # create tensorflow structure
    y1 = add_layer(xs, 600, 256, 'l1', activation_function=tf.nn.sigmoid)
    y2 = add_layer(y1, 256, 64, 'l2', activation_function=tf.nn.sigmoid)
    y3 = add_layer(y2, 64, 1, 'l3', activation_function=tf.nn.sigmoid)

    sess = tf.Session()

    saver = tf.train.Saver()

    # restore model
    saver.restore(sess, "./model/stockModel.ckpt")
    print("restore model sucesss")
    y_pre = sess.run(y3, feed_dict={xs: inputEvent})
    print(y_pre)
    return y_pre


# =============================predict model end=======================================

if __name__ == '__main__':
    tmp_input = np.random.random([1, 3 * 100])
    tmp_event = loadEventModel(tmp_input)
    print(len(tmp_event[0]))
    # # tmp_input2 = np.random.random([1, 600])
    # loadStockModel(tmp_input2)
