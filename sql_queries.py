general_ranking_sql = """
  SELECT au.username, count(mmc.user_id) as right_choices
  FROM movies_moviecategory mmc
  INNER JOIN 
  (
    SELECT category_id, movie_id FROM movies_moviecategory
    WHERE user_id = 8
  ) AS ans
  ON ans.category_id = mmc.category_id AND ans.movie_id = mmc.movie_id
  inner join auth_user au on au.id = mmc.user_id
  group  by au.username 
  order by right_choices;
"""

tec_ranking_sql = """
  SELECT au.username, count(mmc.user_id) as right_choices
  FROM movies_moviecategory mmc
  INNER JOIN 
  (
    SELECT category_id, movie_id FROM movies_moviecategory
    WHERE user_id = 8
  ) AS ans
  ON ans.category_id = mmc.category_id AND ans.movie_id = mmc.movie_id
  inner join auth_user au on au.id = mmc.user_id
  where mmc.category_id in (22, 23, 17, 6, 7, 13, 14, 20, 21, 8, 11)
  group  by au.username 
  order by right_choices;
"""

main_ranking_sql = """
  SELECT au.username, count(mmc.user_id) as right_choices
  FROM movies_moviecategory mmc
  INNER JOIN 
  (
    SELECT category_id, movie_id FROM movies_moviecategory
    WHERE user_id = 8
  ) AS ans
  ON ans.category_id = mmc.category_id AND ans.movie_id = mmc.movie_id
  inner join auth_user au on au.id = mmc.user_id
  where mmc.category_id in (1, 2, 3, 4, 5, 12, 15, 16)
  group  by au.username 
  order by right_choices;
"""

lucky_ranking_sql = """
  SELECT au.username, count(mmc.user_id) as right_choices
  FROM movies_moviecategory mmc
  INNER JOIN 
  (
    SELECT category_id, movie_id FROM movies_moviecategory
    WHERE user_id = 8
  ) AS ans
  ON ans.category_id = mmc.category_id AND ans.movie_id = mmc.movie_id
  inner join auth_user au on au.id = mmc.user_id
  where mmc.category_id in (9, 10, 18, 19)
  group  by au.username 
  order by right_choices;
"""

random_bets_sql = """
  select au.username, description  from movies_randombet mr
  inner join auth_user au 
  on au.id = mr.user_id;
"""

ai_descriptions_sql = """
  select au.username, image from profiles_userprofile pu 
  inner join auth_user au 
  on au.id = pu.user_id ;
"""