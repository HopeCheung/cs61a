CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name as name, b.size as size from dogs as a, sizes as b 
  where a.height > b.min and a.height <= b.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT a.child from parents as a, dogs as b 
  where a.parent = b.name order by b.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as first, b.child as second
  from parents as a, parents as b
  where a.parent = b.parent and a.child < b.child; 

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT s.first ||' and '||s.second ||' are '||r1.size ||' siblings' 
  from siblings as s, size_of_dogs as r1, size_of_dogs as r2
  where first = r1.name  and second = r2.name and r1.size = r2.size;
-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);
  
-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  WITH stacks(dogs, count, stack_height, last_height) AS ( 
    SELECT name, 1, height, height from dogs union
    SELECT dogs || ', ' || name, count+1, stack_height + height, height
    from stacks, dogs
    where count < 4 and height > last_height
  )
  SELECT dogs, stack_height from stacks where stack_height >= 170 order by stack_height;

