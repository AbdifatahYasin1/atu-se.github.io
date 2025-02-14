# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 1.0.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

load_ext sql

# %%sql 
mysql+pymysql://instructor:password@localhost/
drop database if exists lecture2;
create database lecture2;
use lecture2;

# # Create Table Construct

# %%sql
create table instructor (
    ID         char(5),
    name       varchar(20),
    dept_name  varchar(20),
    salary     numeric(8,2)
)


# # List Tables
#
# If you want to show the tables in your database, use the `show tables` command.

# %%sql 
show tables;

# %%sql 
create table department (
     dept_name varchar(20),
     primary key (dept_name)
);

# %%sql 
show tables;

# # Describe Tables
#
# If you want to see a description of a table, use the `desc <tablename>` command.

# %%sql 
desc instructor;

# %%sql 
desc department;

# # Delete Table
#

# %%sql 
drop table instructor;

# What happens if you try to drop a table that doesn't exist?

# %%sql 
drop table offices;

# So we have an alternative syntax that will drop it if it exists:

# %%sql 
drop table if exists offices;

# %%sql 
show tables;

# # Integrity Constraints in Create Table
#
# * not null
# * primary key 
# * foreign key

# ## Not Null

# %%sql
drop table if exists instructor;
create table instructor (
    ID         char(5),
    name       varchar(20) not null,
    dept_name  varchar(20),
    salary     numeric(8,2)
);

# %%sql 
desc instructor;

# # Primary Key

# %%sql
drop table if exists instructor;
create table instructor (
    ID         char(5),
    name       varchar(20) not null,
    dept_name  varchar(20),
    salary     numeric(8,2),
    primary key (ID)
);

# # Foreign Key

# %%sql
drop table if exists instructor;
create table instructor (
    ID         char(5),
    name       varchar(20) not null,
    dept_name  varchar(20),
    salary     numeric(8,2),
    primary key (ID),
    foreign key (dept_name) references department (dept_name)
);

# %%sql 
desc instructor;

# # More Relation Definitions

# %%sql 
drop table if exists student;
create table student (
    ID                 varchar(5),
    name               varchar(20) not null,
    dept_name          varchar(20),
    tot_cred           numeric(3,0),
    primary key (ID),
    foreign key (dept_name) references department(dept_name)
);


# %%sql 
drop table if exists course;
create table course (
    course_id        varchar(8)  ,
    title            varchar(50) ,
    dept_name        varchar(20) ,
    credits          numeric(2,0),
    primary key (course_id),
    foreign key (dept_name) references department(dept_name)
);

# %%sql 
show tables;


