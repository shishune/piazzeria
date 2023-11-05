# source: https://github.com/hfaran/piazza-api 
from piazza_api import Piazza
import json
import pandas 


p = Piazza()
p.user_login("Eryka.shishun@mail.utoronto.ca", "newhacks2023")

# Email: Eryka.shishun@mail.utoronto.ca
# Password: newhacks2023

user_profile = p.get_user_profile()
# print(user_profile)

mat137  = p.network("jyumkm04gce137")

# csc108  = p.network("jze9t3lhrrr29h")


print("\nPOST!!!\n")



def load_all_posts_to_df(course):
    all_posts = course.iter_all_posts(limit=50)
    i = 0
    post_df = pandas.DataFrame(columns=('nr', 'folders', "type", "tags", "history", "children", "tag_good"))
    for post in all_posts:
        post_df.loc[i] = [post["nr"], post["folders"], post["type"], post["tags"], post["history"], post["children"], post["tag_good"]]
        i+= 1
    return post_df

def get_all_folders(post_df):
    folder_list = post_df["folders"].values.tolist()
    print(folder_list)
    flatten_list = [j for sub in folder_list for j in sub]
    print(flatten_list)
    return set(flatten_list)


# post_df = load_all_posts_to_df(mat137)
# # print(post_df)
# folders = get_all_folders(post_df)
# print(folders)


nr = 1954
folder_filters = mat137.feed_filters
# print(folder_filters)
# print(folder_filters[2]())

filtered_posts = mat137.get_filtered_feed(folder_filters[2]("test1"))

feed_posts = filtered_posts["feed"]
# print(feed_posts)
# posts = [mat137.get_post(nr)]
# posts = mat137.iter_all_posts(limit=50)

print("\n\nParse\n")
# def convert(generator):
#    required_info_lst = ["folders", "nr", "type", "tags", "history", "children"]
#    res_dict = {}
#    i = 0
#    for item in generator:
#         item_info = {}
#         for required_info in required_info_lst:
#             # print("required info: " + required_info)
#             # print(item[required_info])
#             # print()
#             item_info[required_info] = item[required_info]

#         item_info["tag_good"] = len(item["tag_good"])
    
#         res_dict[i] = item_info
#         i += 1 
# #    print(res_dict)
#    return res_dict


# def convert2(generator):
#    required_info_lst = ["nr", "type", "tags", "history", "children"]
#    res_dict = {}
#    i = 0
#    for item in generator:
#         res_dict[i] = item
#         # print(item)
#         i += 1 
# #    print(res_dict)
#    return res_dict
 
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

    
# posts_dict = convert(posts)
# print(posts_dict)

# with open('piazzeria/test/parsed_posts.json', 'w', encoding='utf-8') as f:
#     json.dump(posts_dict, f, ensure_ascii=False, indent=4)

# print(type(feed_posts))


feed_posts_list = find_credible_filtered_posts(feed_posts, good_q=False)
# print(feed_posts_list)

good_feed_posts_list = find_credible_filtered_posts(feed_posts)
# print(good_feed_posts_list)

def find_endorsed_student_answer(children_list):
    for child in children_list:
        if child["type"] == "s_answer":
    #  check if student answer
    # check who has endorsed it 
            # for endorser in child["tag_endorse"]:
            #     if(endorser["role"] == "instructor" or endorser["role"] == "ta"): 
    #  check if a ta or instructor has endorsed this question 
    # realizing that the above is not necessary because the filtered posts should already only include prof indorsed student answers..

    # then return. else do not return 
            return child["history"][0]["content"]
    

def find_instructor_answer(children_list):
    for child in children_list:
        if child["type"] == "i_answer":
    # then return. else do not return 
            return child["history"][0]["content"]

def get_post_details_list(course, post_ids_list):
    post_details_list = []
    for post_id in post_ids_list:
        post_info = course.get_post(post_id)
        # print(post_info)
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
        
print("\n\n")
post_details = get_post_details_list(mat137, good_feed_posts_list)
print(post_details)




# feed_posts_dict = convert2(feed_posts)
# print(feed_posts_dict)

# with open('piazzeria/test/feed_parsed_posts.json', 'w', encoding='utf-8') as f:
#     json.dump(feed_posts_dict, f, ensure_ascii=False, indent=4)

# for post in posts:
#     print(post)

# users = mat137.get_users(["userid1", "userid2"])
# all_users = mat137.get_all_users()
# print(all_users)
