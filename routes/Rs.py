from firebase_admin import auth, db
from . import routes
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

'''
1. modify algo "store user data in db and change it only when profile changes"
2. get user data
3. modify return
'''
@routes.route('/rs')
def index():
    courses = db.reference(path='courses').get()
    # users = db.reference(path='users').get()

    cfList = []

    for df in courses:
        # df = courses[key]
        print(df)

        for feature in features:
            if (df[feature] == None):
                df[feature] = ' '

        # combine keywords and genres
        df["combined_features"] = combine_features(df)

        # courses[key] = df
        cfList.append(df["combined_features"])

    return {
        "courses": courses,
        "cfList": cfList,

    };
    print(cfList)

    # define CountVectorizer module
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(cfList)

    cosine_sim = cosine_similarity(count_matrix)

    print("cosine_sim")
    print(cosine_sim)
    print("jaksbdkjasbdkjs")
    print(len(cosine_sim))

    user_likes = "The Ultimate Guide to Game Development with Unity 2019"

    index = get_index_from_title(user_likes)
    print("asd as dsa dd s")
    print(cosine_sim[int(index)])
    print("index")
    print(index)

    similar = list(enumerate(cosine_sim[int(index)]))

    print("similar")
    print(similar)

    sorted_similar = sorted(similar, key=lambda x: x[1], reverse=True)[1:]

    print("sorted_similar")
    print(sorted_similar)

    i = 0
    print("Top 5 similar to "+user_likes+" are:\n")

    result = []
    for element in sorted_similar:
        print(get_title_from_index(element[0], courses))

        result.append( get_title_from_index(element[0], courses))
        

        i = i+1
        if i > 5:
            break

    return {
        "result": result
    }

features = ['keywords', 'genres']
def combine_features(row):
    return row['keywords']+" "+row['genres']


def get_title_from_index(index, courses):
    # return df[df.index == index]["title"].values[0]
    return courses[index]["title"]


def get_index_from_title(title):
    # return df[df.title == title]["index"].values[0]

    course = db.reference(path='courses').order_by_child(
        'title').equal_to(title).get()

    key = None
    for key in course:
        print(key)

    return key
