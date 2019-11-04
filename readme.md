Available attributes -  
  
  
| Name | Type |
| ---- | ----- |
color           |            string  |
director_name    |           string  |
num_critic_for_reviews   |   integer |
duration                 |  integer  |
director_facebook_likes  |  integer  |
actor_3_facebook_likes   |  integer  |
actor_2_name             |  string   |
actor_1_facebook_likes   |  integer  |
gross                    |  integer  |
genres                   |  string   |
actor_1_name             |  string   |
movie_title              |  string   |
num_voted_users          |  integer  |
cast_total_facebook_likes |  integer |
actor_3_name             |  string   |
facenumber_in_poster     |  integer  |
plot_keywords            |  string   |
movie_imdb_link          |  url      |
num_user_for_reviews     |  integer  |
language                 |  string   |
country                  |  string   |
content_rating           |  string   |
budget                   |  integer  |
title_year               |  year     |
actor_2_facebook_likes   |  integer  |
imdb_score               |  decimal  |
aspect_ratio             |  decimal  |
movie_facebook_likes     |  integer  |

Based on some analysis we've come to the conclusion that the required attributes that majorly affect movie ratings are-

| attributes | ratings |
|------------|---------|
imdb_score  | 83.212161269  |
num_critic_for_reviews  |  |
duration  |  |
director_facebook_likes  |  |
actor_1_facebook_likes  |  |
actor_2_facebook_likes  |  |
actor_3_facebook_likes  |  |
cast_total_facebook_likes  |  |
movie_facebook_likes  |  |
num_voted_users  |  |
budget  |  |
gross  |  |
  |  |
imdb_score  | 83.212161269  |
num_critic_for_reviews  |     |
duration  |     |
director_facebook_likes  |    |
actor_3_facebook_likes  |    |
cast_total_facebook_likes  |    |
movie_facebook_likes  |    |
num_voted_users  |    |
budget  |    |
gross  |   |
  |   |
imdb_score  | 82.8816920026  |
num_critic_for_reviews  |  |
duration  |  |
actor_1_facebook_likes  |  |
actor_2_facebook_likes  |  |
actor_3_facebook_likes  |  |
cast_total_facebook_likes  |  |
movie_facebook_likes  |  |
num_voted_users  |  |
  |    |
imdb_score  | 81.8241903503  |
num_critic_for_reviews  |  |
duration  |  |
actor_1_facebook_likes  |  |
actor_2_facebook_likes  |  |
actor_3_facebook_likes  |  |
cast_total_facebook_likes  |  |
  |    |
imdb_score  | 81.8241903503  |
num_critic_for_reviews  |  |
duration  |  |
  |   |


### Conclusion
- Also, we have gone for a +1 -1 prediction for a round of value over here.
- Finally it was observed that movie ratings is a highly volatile thing and can depend on many attributes as seen from the results above.

