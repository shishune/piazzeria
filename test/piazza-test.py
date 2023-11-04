# source: https://github.com/hfaran/piazza-api 
from piazza_api import Piazza
p = Piazza()
p.user_login("Eryka.shishun@mail.utoronto.ca", "newhacks2023")

# Email: Eryka.shishun@mail.utoronto.ca
# Password: newhacks2023

user_profile = p.get_user_profile()
# print(user_profile)

mat137  = p.network("jyumkm04gce137")
# print("MAT137")
# print(mat137)

print("\nPOST!!!\n")
print(mat137.get_post(190))


posts = mat137.iter_all_posts(limit=10)

# for post in posts:
#     print(post)

# users = mat137.get_users(["userid1", "userid2"])
# all_users = mat137.get_all_users()
# print(all_users)
