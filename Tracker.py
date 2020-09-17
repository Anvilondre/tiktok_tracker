import sched
import time
import numpy as np
import matplotlib.pyplot as plt
from TikTokAPI import TikTokAPI
from account_id import account_id


def do_something(sc, iterations=[], subs_history=[], likes_history=[]):
    # Get data
    user = api.getUserByName(account_id)['userInfo']['stats']
    subs, likes = int(user['followerCount']), int(user['heartCount'])
    print("Subs: {}, likes: {}".format(subs, likes))

    # Add to history
    subs_history = np.append(subs_history, subs)
    likes_history = np.append(likes_history, likes)
    iterations = np.append(iterations, iterations[-1] + 1)

    # Subs
    plt.figure(0)
    plt.plot(iterations, subs_history)
    plt.ylabel('Subscribers')
    plt.xlabel('Time (minutes)')
    plt.savefig('subs_fig.png')

    # Likes
    plt.figure(1)
    plt.plot(iterations, likes_history)
    plt.ylabel('Likes')
    plt.xlabel('Time (minutes)')
    plt.savefig('likes_fig.png')

    # Save data
    np.savetxt('likes.csv', likes_history, delimiter=',')
    np.savetxt('subs.csv', subs_history, delimiter=',')
    np.savetxt('iterations.csv', iterations, delimiter=',')

    s.enter(60, 1, do_something, (sc, iterations, subs_history, likes_history))


if __name__ == '__main__':
    print('File loaded!')
    api = TikTokAPI()
    iters = np.loadtxt('iterations.csv')
    subs_hist = np.loadtxt('subs.csv')
    likes_hist = np.loadtxt('likes.csv')
    s = sched.scheduler(time.time, time.sleep)
    s.enter(0, 1, do_something, (s, iters, subs_hist, likes_hist))
    s.run()
