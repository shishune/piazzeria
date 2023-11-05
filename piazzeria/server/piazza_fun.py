from piazza_api import Piazza
import pandas

# not in use
def load_all_posts_to_df(course):
    all_posts = course.iter_all_posts(limit=50)
    i = 0
    post_df = pandas.DataFrame(columns=('nr', 'folders', "type", "tags", "history", "children", "tag_good"))
    for post in all_posts:
        post_df.loc[i] = [post["nr"], post["folders"], post["type"], post["tags"], post["history"], post["children"], post["tag_good"]]
        i+= 1
    return post_df

# def get_all_folders(post_df):
#     folder_list = post_df["folders"].values.tolist()
#     print(folder_list)
#     flatten_list = [j for sub in folder_list for j in sub]
#     print(flatten_list)
#     return set(flatten_list)

def get_all_folders(course_id):
    if course_id == "jyumkm04gce137": # mat137
        return ["ps1", "ps2", "ps3", "ps4","ps5","ps6","ps7","ps8","ps9", "ps10", "test1", "test2", "test3", "test4", "final", "logistics", "lecture", "tutorial", "other"]
    elif course_id == "jze9t3lhrrr29h": #csc108
        return [ "assignment1", "assignment2", "assignment3", "lecture",  "prepare", "rehearse", "midterm_exam", "exam"]
    return ["lecture", "tutorial", "a1", "a2", "a3"]

def find_credible_filtered_posts(posts_list, good_q=True):
    credible_posts_nr = []
    for post in posts_list:
        try: 
            if (post["has_i"] or (post["has_s"]  and post["tag_endorse_prof"] )):
                if (good_q and post["gd"]  > 0):
                    credible_posts_nr.append(post["nr"])
                elif (not good_q):
                    credible_posts_nr.append(post["nr"])
        
        except KeyError:
            continue

    return credible_posts_nr


def find_endorsed_student_answer(children_list):
    for child in children_list:
        if child["type"] == "s_answer":
    #  check if student answer
    # then return. else do not return 
            return child["history"][0]["content"]
    

def find_instructor_answer(children_list):
    for child in children_list:
        if child["type"] == "i_answer":
            return child["history"][0]["content"]

def get_post_details_list(course, post_ids_list):
    post_details_list = []
    for post_id in post_ids_list:
        post_info = course.get_post(post_id)
        post_details = {}
        post_details["id" ] = post_info["nr"]
        post_details["folders"] = post_info["folders"]
        post_details["title"] = post_info["history"][0]["subject"]
        post_details["question"] = post_info["history"][0]["content"]
        post_details["s_answer"] = find_endorsed_student_answer(post_info["children"])
        post_details["i_answer"] = find_instructor_answer(post_info["children"])
        post_details_list.append(post_details)
        
        # post_details[""] = post_info[""]
    return post_details_list

