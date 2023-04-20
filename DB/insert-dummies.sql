\connect ioproject admin_user;

--bin
INSERT INTO public.bin VALUES (1, NULL, '2023-03-04 11:00:00', NULL);
INSERT INTO public.bin VALUES (2, NULL, '2023-03-05 12:00:00', NULL);
INSERT INTO public.bin VALUES (3, NULL, '2023-03-06 13:00:00', NULL);
INSERT INTO public.bin VALUES (4, NULL, '2023-03-07 14:00:00', NULL);
INSERT INTO public.bin VALUES (5, NULL, '2023-03-08 15:00:00', NULL);
INSERT INTO public.bin VALUES (6, NULL, '2023-03-09 15:00:00', NULL);
INSERT INTO public.bin VALUES (7, NULL, '2023-03-09 15:00:00', NULL);
INSERT INTO public.bin VALUES (8, NULL, '2023-03-09 15:00:00', NULL);
INSERT INTO public.bin VALUES (9, NULL, '2023-03-09 15:00:00', NULL);
INSERT INTO public.bin VALUES (10, NULL, '2023-03-10 15:00:00', NULL);

--catalog
INSERT INTO public.catalog VALUES (1, '2023-03-04 10:00:00');
INSERT INTO public.catalog VALUES (2, '2023-03-05 11:00:00');
INSERT INTO public.catalog VALUES (3, '2023-03-06 12:00:00');
INSERT INTO public.catalog VALUES (4, '2023-03-07 13:00:00');
INSERT INTO public.catalog VALUES (5, '2023-03-08 14:00:00');
INSERT INTO public.catalog VALUES (6, '2023-03-08 14:00:00');
INSERT INTO public.catalog VALUES (7, '2023-03-08 15:00:00');
INSERT INTO public.catalog VALUES (8, '2023-03-08 16:00:00');
INSERT INTO public.catalog VALUES (9, '2023-03-09 17:00:00');
INSERT INTO public.catalog VALUES (10, '2023-03-10 14:00:00');

--note
INSERT INTO public.note VALUES (1, NULL, 'titletest', 'desctest', 'bodytest', '2023-03-04 01:00:00', '2023-03-04 02:00:00');
INSERT INTO public.note VALUES (2, NULL, 'titletest2', 'desctest2', 'bodytest2', '2023-03-05 02:00:00', '2023-03-05 03:00:00');
INSERT INTO public.note VALUES (3, NULL, 'titletest3', 'desctest3', 'bodytest3', '2023-03-06 03:00:00', '2023-03-06 04:00:00');
INSERT INTO public.note VALUES (4, NULL, 'titletest4', 'desctest4', 'bodytest4', '2023-03-07 04:00:00', '2023-03-07 05:00:00');
INSERT INTO public.note VALUES (5, NULL, 'titletest5', 'desctest5', 'bodytest5', '2023-03-08 05:00:00', '2023-03-08 06:00:00');
INSERT INTO public.note VALUES (6, NULL, 'titletest6', 'desctest6', 'bodytest6', '2023-03-08 05:00:00', '2023-03-08 06:00:00');
INSERT INTO public.note VALUES (7, NULL, 'titletest7', 'desctest7', 'bodytest7', '2023-03-09 05:00:00', '2023-03-09 06:00:00');
INSERT INTO public.note VALUES (8, NULL, 'titletest8', 'desctest8', 'bodytest8', '2023-03-10 05:00:00', '2023-03-10 06:00:00');
INSERT INTO public.note VALUES (9, NULL, 'titletest9', 'desctest9', 'bodytest9', '2023-03-11 05:00:00', '2023-03-11 06:00:00');
INSERT INTO public.note VALUES (10, NULL, 'titletest10', 'desctest10', 'bodytest10', '2023-03-12 05:00:00', '2023-12-08 06:00:00');

--tag
INSERT INTO public.tag VALUES (1, 'tagtest');
INSERT INTO public.tag VALUES (2, 'tagtest2');
INSERT INTO public.tag VALUES (3, 'tagtest3');
INSERT INTO public.tag VALUES (4, 'tagtest4');
INSERT INTO public.tag VALUES (5, 'tagtest5');
INSERT INTO public.tag VALUES (6, 'tagtest6');
INSERT INTO public.tag VALUES (7, 'tagtest7');
INSERT INTO public.tag VALUES (8, 'tagtest8');
INSERT INTO public.tag VALUES (9, 'tagtest9');
INSERT INTO public.tag VALUES (10, 'tagtest10');

--user_table
INSERT INTO public.user_table VALUES (1, 'user1', 'testtest', 'testtest@test.com', 1, '2023-03-04 18:55:55');
INSERT INTO public.user_table VALUES (2, 'user2', 'testtest2', 'testtest2@test.com', 2, '2023-03-05 18:55:55');
INSERT INTO public.user_table VALUES (3, 'user3', 'testtest3', 'testtest3@test.com', 1, '2023-03-06 18:55:55');
INSERT INTO public.user_table VALUES (4, 'user4', 'testtest4', 'testtest4@test.com', 2, '2023-03-07 18:55:55');
INSERT INTO public.user_table VALUES (5, 'user5', 'testtest5', 'testtest5@test.com', 1, '2023-03-08 18:55:55');
INSERT INTO public.user_table VALUES (6, 'user6', 'testtest6', 'testtest6@test.com', 1, '2023-03-09 18:55:55');
INSERT INTO public.user_table VALUES (7, 'user7', 'testtest7', 'testtest7@test.com', 1, '2023-03-09 18:55:55');
INSERT INTO public.user_table VALUES (8, 'user8', 'testtest8', 'testtest8@test.com', 1, '2023-03-10 18:55:55');
INSERT INTO public.user_table VALUES (9, 'user9', 'testtest9', 'testtest9@test.com', 1, '2023-03-10 18:55:55');
INSERT INTO public.user_table VALUES (10, 'user10', 'testtest10', 'testtest10@test.com', 1, '2023-03-11 18:55:55');

--note_tag
INSERT INTO public.note_tag VALUES (1, 1, 1);
INSERT INTO public.note_tag VALUES (2, 1, 2);
INSERT INTO public.note_tag VALUES (3, 2, 3);
INSERT INTO public.note_tag VALUES (4, 3, 5);
INSERT INTO public.note_tag VALUES (5, 4, 3);
INSERT INTO public.note_tag VALUES (6, 1, 3);
INSERT INTO public.note_tag VALUES (7, 5, 2);
INSERT INTO public.note_tag VALUES (8, 7, 3);
INSERT INTO public.note_tag VALUES (9, 8, 3);
INSERT INTO public.note_tag VALUES (10, 9, 5);

--user_note
INSERT INTO public.user_note VALUES (1, 1, 2);
INSERT INTO public.user_note VALUES (2, 1, 4);
INSERT INTO public.user_note VALUES (3, 2, 3);
INSERT INTO public.user_note VALUES (4, 4, 5);
INSERT INTO public.user_note VALUES (5, 5, 1);
INSERT INTO public.user_note VALUES (6, 2, 1);
INSERT INTO public.user_note VALUES (7, 3, 2);
INSERT INTO public.user_note VALUES (8, 7, 4);
INSERT INTO public.user_note VALUES (9, 8, 5);
INSERT INTO public.user_note VALUES (10, 3, 5);



