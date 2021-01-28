-- 新建数据库，然后执行下面sql
CREATE TABLE message(
	id PRIMARY KEY not null,
	name VARCHAR(60) not null, 
	body VARCHAR(200) not null, 
	create_at DATETIME
);