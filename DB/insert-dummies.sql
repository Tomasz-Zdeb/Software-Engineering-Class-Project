--bin
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-04 11:00:00', NULL);
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-05 12:00:00', NULL);
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-06 13:00:00', NULL);
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-07 14:00:00', NULL);
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-08 15:00:00', NULL);
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-09 15:00:00', NULL);
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-09 15:00:00', NULL);
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-09 15:00:00', NULL);
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-09 15:00:00', NULL);
INSERT INTO public.bin VALUES (DEFAULT, NULL, '2023-03-10 15:00:00', NULL);

--catalog
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-04 10:00:00');
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-05 11:00:00');
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-06 12:00:00');
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-07 13:00:00');
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-08 14:00:00');
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-08 14:00:00');
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-08 15:00:00');
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-08 16:00:00');
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-09 17:00:00');
INSERT INTO public.catalog VALUES (DEFAULT, '2023-03-10 14:00:00');

--note
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest', 'desctest', 'bodytest', '2023-03-04 01:00:00', '2023-03-04 02:00:00');
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest2', 'desctest2', 'bodytest2', '2023-03-05 02:00:00', '2023-03-05 03:00:00');
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest3', 'desctest3', 'bodytest3', '2023-03-06 03:00:00', '2023-03-06 04:00:00');
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest4', 'desctest4', 'bodytest4', '2023-03-07 04:00:00', '2023-03-07 05:00:00');
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest5', 'desctest5', 'bodytest5', '2023-03-08 05:00:00', '2023-03-08 06:00:00');
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest6', 'desctest6', 'bodytest6', '2023-03-08 05:00:00', '2023-03-08 06:00:00');
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest7', 'desctest7', 'bodytest7', '2023-03-09 05:00:00', '2023-03-09 06:00:00');
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest8', 'desctest8', 'bodytest8', '2023-03-10 05:00:00', '2023-03-10 06:00:00');
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest9', 'desctest9', 'bodytest9', '2023-03-11 05:00:00', '2023-03-11 06:00:00');
INSERT INTO public.note VALUES (DEFAULT, NULL, 'titletest10', 'desctest10', 'bodytest10', '2023-03-12 05:00:00', '2023-12-08 06:00:00');

--tag
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest');
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest2');
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest3');
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest4');
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest5');
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest6');
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest7');
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest8');
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest9');
INSERT INTO public.tag VALUES (DEFAULT, 'tagtest10');

--user_table
INSERT INTO public.user_table VALUES (DEFAULT, 'user1', 'testtest', 'testtest@test.com', 1, '2023-03-04 18:55:55');
INSERT INTO public.user_table VALUES (DEFAULT, 'user2', 'testtest2', 'testtest2@test.com', 2, '2023-03-05 18:55:55');
INSERT INTO public.user_table VALUES (DEFAULT, 'user3', 'testtest3', 'testtest3@test.com', 1, '2023-03-06 18:55:55');
INSERT INTO public.user_table VALUES (DEFAULT, 'user4', 'testtest4', 'testtest4@test.com', 2, '2023-03-07 18:55:55');
INSERT INTO public.user_table VALUES (DEFAULT, 'user5', 'testtest5', 'testtest5@test.com', 1, '2023-03-08 18:55:55');
INSERT INTO public.user_table VALUES (DEFAULT, 'user6', 'testtest6', 'testtest6@test.com', 1, '2023-03-09 18:55:55');
INSERT INTO public.user_table VALUES (DEFAULT, 'user7', 'testtest7', 'testtest7@test.com', 1, '2023-03-09 18:55:55');
INSERT INTO public.user_table VALUES (DEFAULT, 'user8', 'testtest8', 'testtest8@test.com', 1, '2023-03-10 18:55:55');
INSERT INTO public.user_table VALUES (DEFAULT, 'user9', 'testtest9', 'testtest9@test.com', 1, '2023-03-10 18:55:55');
INSERT INTO public.user_table VALUES (DEFAULT, 'user10', 'testtest10', 'testtest10@test.com', 1, '2023-03-11 18:55:55');

--note_tag
INSERT INTO public.note_tag VALUES (DEFAULT, 1, 1);
INSERT INTO public.note_tag VALUES (DEFAULT, 1, 2);
INSERT INTO public.note_tag VALUES (DEFAULT, 2, 3);
INSERT INTO public.note_tag VALUES (DEFAULT, 3, 5);
INSERT INTO public.note_tag VALUES (DEFAULT, 4, 3);
INSERT INTO public.note_tag VALUES (DEFAULT, 1, 3);
INSERT INTO public.note_tag VALUES (DEFAULT, 5, 2);
INSERT INTO public.note_tag VALUES (DEFAULT, 7, 3);
INSERT INTO public.note_tag VALUES (DEFAULT, 8, 3);
INSERT INTO public.note_tag VALUES (DEFAULT, 9, 5);

--user_note
INSERT INTO public.user_note VALUES (DEFAULT, 1, 2);
INSERT INTO public.user_note VALUES (DEFAULT, 1, 4);
INSERT INTO public.user_note VALUES (DEFAULT, 2, 3);
INSERT INTO public.user_note VALUES (DEFAULT, 4, 5);
INSERT INTO public.user_note VALUES (DEFAULT, 5, 1);
INSERT INTO public.user_note VALUES (DEFAULT, 2, 1);
INSERT INTO public.user_note VALUES (DEFAULT, 3, 2);
INSERT INTO public.user_note VALUES (DEFAULT, 7, 4);
INSERT INTO public.user_note VALUES (DEFAULT, 8, 5);
INSERT INTO public.user_note VALUES (DEFAULT, 3, 5);



