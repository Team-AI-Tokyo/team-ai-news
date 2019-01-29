use AI;
alter table AINews
add NewsID int identity(1,1) Primary key;

alter table AINews
add NewsSource varchar(100);

update AInews
set NewsSource = 'Kaggle'
where NewsSource is null;


alter table AINews
add SourceID int;

update AINews
set SourceID  = 1
where SourceID is null;

insert into newssource (sourcename)
values
('Kaggle');

alter table AINews
add foreign key (SourceID) REFERENCES newssource(sourceID);