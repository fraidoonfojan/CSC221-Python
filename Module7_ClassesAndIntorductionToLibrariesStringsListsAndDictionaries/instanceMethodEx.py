'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
my_video1 and my_video2 are instances of the Video class. 
Attribute like_clicks of both my_video1 and my_video2 is initialized with 0. 
In the Video class, define instance method like() with 
self as the parameter to increment attribute like_clicks 
and output 'Thank you for liking this video.'


'''


class Video:
    def __init__(self):
        self.like_clicks = 0

    def like(self):
        self.like_clicks += 1
        print("Thank you for liking this video.")

# Create two instances of the Video class
my_video1 = Video()
my_video2 = Video()

# Read the number of likes for each video
likes_video1 = int(input())
likes_video2 = int(input())

# Apply likes to my_video1
for _ in range(likes_video1):
    my_video1.like()

# Apply likes to my_video2
for _ in range(likes_video2):
    my_video2.like()

# Output the total number of likes for each video
print(f"The first video is liked {my_video1.like_clicks} time(s).")
print(f"The second video is liked {my_video2.like_clicks} time(s).")