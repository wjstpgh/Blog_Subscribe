CREATE TABLE user_info
(
    USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    USER_EMAIL VARCHAR(100) NOT NULL,
    BLOG_ID CHAR(4),
    PRIMARY KEY(USER_ID)
);
-- user_info 테이블 생성
-- user_id를 기본키로 가지고 생성될때마다 자동적으로 수를 증가시켜 인덱싱을 함
-- USER_EMAIL로 사용자의 이메일 주소를 관리
-- BLOG_ID로 사용자가 구독한 블로그 페이지를 관리