create database AI

use AI
create table newssource(
sourceID int identity(1,1) primary key,
sourcename nvarchar(255) not null,
);

create table AInews(
articleID int identity(1,1) Primary key,
sourceID int FOREIGN KEY REFERENCES newssource(sourceID),
Title nvarchar(255) not null,
news_Description nvarchar(255),
newsUrl nvarchar(255) unique,
Author nvarchar(255)
); 

 