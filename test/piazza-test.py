# source: https://github.com/hfaran/piazza-api 
from piazza_api import Piazza
import json



p = Piazza()
p.user_login("Eryka.shishun@mail.utoronto.ca", "newhacks2023")

# Email: Eryka.shishun@mail.utoronto.ca
# Password: newhacks2023

user_profile = p.get_user_profile()
# print(user_profile)

mat137  = p.network("jyumkm04gce137")
print("MAT137")
print(mat137)

# csc108  = p.network("jze9t3lhrrr29h")


print("\nPOST!!!\n")
nr = 1954
folder_filters = mat137.feed_filters
print(folder_filters)

posts = mat137.get_filtered_feed(folder_filters[2]("ps1"))
print(posts)
# posts = [mat137.get_post(nr)]
# posts = mat137.iter_all_posts(limit=50)

print("\n\nParse\n")
def convert(generator):
   required_info_lst = ["nr", "type", "tags", "history", "children"]
   res_dict = {}
   i = 0
   for item in generator:
        item_info = {}
        for required_info in required_info_lst:
            print("required info: " + required_info)
            print(item[required_info])
            print()
            item_info[required_info] = item[required_info]

        item_info["tag_good"] = len(item["tag_good"])
    
        res_dict[i] = item_info
        i += 1 
#    print(res_dict)
   return res_dict


def convert2(generator):
   required_info_lst = ["nr", "type", "tags", "history", "children"]
   res_dict = {}
   i = 0
   for item in generator:
        res_dict[i] = item
        print(item)
        i += 1 
#    print(res_dict)
   return res_dict
 
posts_dict = convert2(posts)
print(posts_dict)

with open('piazzeria/test/parsed_posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts_dict, f, ensure_ascii=False, indent=4)

# for post in posts:
#     print(post)

# users = mat137.get_users(["userid1", "userid2"])
# all_users = mat137.get_all_users()
# print(all_users)
