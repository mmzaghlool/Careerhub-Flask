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
@routes.route('/rs/<uid>', methods=['GET'])
def index(uid=None):
    courses = db.reference(path='courses').get()
    userGroups = db.reference(path='users/{0}/groups'.format(uid)).get()
    # print(courses)
    print(userGroups)

    cfList = []
    for df in courses:
        if df == 'x':
            continue
        df = courses[df]

        for feature in features:
            if (df[feature] == None):
                df[feature] = ' '

        # combine keywords and genres
        df["combined_features"] = combine_features(df)

        # courses[key] = df
        cfList.append(df["combined_features"])

    # print("cfList", cfList)

    # define CountVectorizer module
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(cfList)
    cosine_sim = cosine_similarity(count_matrix)

    user_likes = []
    if userGroups is not None:
        for group in userGroups:
            group = userGroups[group]
            user_likes.append({
                "id": group["courseID"],
                "combined_features": group['keywords']+" "+group['genres']
            })

    # user_likes = ["The Ultimate Guide to Game Development with Unity 2019"]
    
    print("user_likes", user_likes)
    if len(user_likes) > 3 :
        user_likes = user_likes[-3:]

    print("user_likes", user_likes)

    result = []
    for course in user_likes:
        # course_index = get_index_from_title(course)
        similar_courses = list(enumerate(cosine_sim[int(course["id"])]))
        sorted_similar_courses = sorted(
            similar_courses, key=lambda x: x[1], reverse=True)[1:]
        i = 0
        for element in sorted_similar_courses:
            # print(get_title_from_index(element[0], courses))
            result.append(get_title_from_index(element[0], courses))

            i = i+1
            if i > 2:
                break

    return {
        "success": True,
        "result": result
    }


features = ['keywords', 'genres']


def combine_features(row):
    return row['keywords']+" "+row['genres']


def get_title_from_index(index, courses):
    # print(courses)
    # return df[df.index == index]["title"].values[0]
    return courses["{0}".format(index)]


def get_index_from_title(title):
    # return df[df.title == title]["index"].values[0]

    course = db.reference(path='courses').order_by_child(
        'title').equal_to(title).get()

    key = None
    for key in course:
        print(key)

    return key
