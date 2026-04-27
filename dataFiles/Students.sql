-- phpMyAdmin SQL Dump
-- version 5.2.3-1.el9.remi
-- https://www.phpmyadmin.net/
--
-- Generation Time: Apr 27, 2026 at 10:31 AM
-- Server version: 5.7.44-log
-- PHP Version: 8.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
--

-- --------------------------------------------------------

--
-- Table structure for table `Students`
--

CREATE TABLE `Students` (
  `student_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `enrollment_date` date NOT NULL,
  `grade_level` int(11) NOT NULL,
  `enrollment_status` varchar(20) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Students`
--

INSERT INTO `Students` (`student_id`, `first_name`, `last_name`, `date_of_birth`, `gender`, `enrollment_date`, `grade_level`, `enrollment_status`, `email`, `phone_number`) VALUES
(1, 'John', 'Doe', '2011-03-15', 'Male', '2023-09-01', 8, 'Active', 'john.doe@example.com', '555-987-6543'),
(2, 'Robert', 'Johnson', '2010-01-10', 'Male', '2022-08-20', 8, 'Active', 'robert.johnson@example.com', '555-100-0002'),
(3, 'Emily', 'Brown', '2013-11-05', 'Female', '2024-09-10', 5, 'Active', 'emily.brown@example.com', '555-100-0003'),
(4, 'Michael', 'Davis', '2009-07-25', 'Male', '2021-08-01', 9, 'Active', 'michael.davis@example.com', '555-100-0004'),
(5, 'Jessica', 'Miller', '2014-02-14', 'Female', '2024-08-25', 4, 'Active', 'jessica.miller@example.com', '555-100-0005'),
(6, 'William', 'Wilson', '2008-09-30', 'Male', '2021-09-05', 10, 'Active', 'william.wilson@example.com', '555-100-0006'),
(7, 'Ashley', 'Moore', '2015-06-01', 'Female', '2025-09-01', 3, 'Active', 'ashley.moore@example.com', '555-100-0007'),
(8, 'Daniel', 'Taylor', '2007-04-03', 'Male', '2020-08-10', 11, 'Active', 'daniel.taylor@example.com', '555-100-0008'),
(9, 'Sarah', 'Anderson', '2016-01-08', 'Female', '2025-08-15', 2, 'Active', 'sarah.anderson@example.com', '555-100-0009'),
(10, 'Christopher', 'Thomas', '2006-12-19', 'Male', '2019-09-20', 12, 'Active', 'christopher.thomas@example.com', '555-100-0010'),
(11, 'Megan', 'Jackson', '2017-03-22', 'Female', '2025-09-05', 1, 'Active', 'megan.jackson@example.com', '555-100-0011'),
(12, 'James', 'White', '2011-08-11', 'Male', '2023-08-30', 7, 'Active', 'james.white@example.com', '555-100-0012'),
(13, 'Laura', 'Harris', '2012-10-01', 'Female', '2023-09-15', 6, 'Active', 'laura.harris@example.com', '555-100-0013'),
(14, 'Joshua', 'Martin', '2010-02-28', 'Male', '2022-09-01', 8, 'Active', 'joshua.martin@example.com', '555-100-0014'),
(15, 'Nicole', 'Thompson', '2013-09-19', 'Female', '2024-08-20', 5, 'Active', 'nicole.thompson@example.com', '555-100-0015'),
(16, 'Andrew', 'Garcia', '2009-05-02', 'Male', '2021-08-10', 9, 'Active', 'andrew.garcia@example.com', '555-100-0016'),
(17, 'Amanda', 'Martinez', '2014-04-07', 'Female', '2024-09-01', 4, 'Active', 'amanda.martinez@example.com', '555-100-0017'),
(18, 'Ryan', 'Robinson', '2008-07-13', 'Male', '2021-08-25', 10, 'Active', 'ryan.robinson@example.com', '555-100-0018'),
(19, 'Elizabeth', 'Clark', '2015-02-09', 'Female', '2025-08-20', 3, 'Active', 'elizabeth.clark@example.com', '555-100-0019'),
(20, 'Kevin', 'Rodriguez', '2007-11-29', 'Male', '2020-09-10', 11, 'Active', 'kevin.rodriguez@example.com', '555-100-0020'),
(21, 'Melissa', 'Lewis', '2016-04-18', 'Female', '2025-09-15', 2, 'Active', 'melissa.lewis@example.com', '555-100-0021'),
(22, 'Jose', 'Lee', '2006-06-05', 'Male', '2019-08-01', 12, 'Active', 'jose.lee@example.com', '555-100-0022'),
(23, 'Michelle', 'Walker', '2017-01-26', 'Female', '2025-08-10', 1, 'Active', 'michelle.walker@example.com', '555-100-0023'),
(24, 'Edward', 'Hall', '2011-10-09', 'Male', '2023-09-05', 7, 'Active', 'edward.hall@example.com', '555-100-0024'),
(25, 'Stephanie', 'Allen', '2012-12-03', 'Female', '2023-08-20', 6, 'Active', 'stephanie.allen@example.com', '555-100-0025'),
(26, 'Brian', 'Young', '2010-04-20', 'Male', '2022-08-25', 8, 'Active', 'brian.young@example.com', '555-100-0026'),
(27, 'Kimberly', 'Hernandez', '2013-07-11', 'Female', '2024-09-05', 5, 'Active', 'kimberly.hernandez@example.com', '555-100-0027'),
(28, 'George', 'King', '2009-01-18', 'Male', '2021-09-10', 9, 'Active', 'george.king@example.com', '555-100-0028'),
(29, 'Heather', 'Wright', '2014-08-29', 'Female', '2024-08-15', 4, 'Active', 'heather.wright@example.com', '555-100-0029'),
(30, 'Donald', 'Lopez', '2008-03-07', 'Male', '2021-09-01', 10, 'Active', 'donald.lopez@example.com', '555-100-0030'),
(31, 'Deborah', 'Hill', '2015-05-24', 'Female', '2025-08-25', 3, 'Active', 'deborah.hill@example.com', '555-100-0031'),
(32, 'Kenneth', 'Scott', '2007-02-01', 'Male', '2020-08-05', 11, 'Active', 'kenneth.scott@example.com', '555-100-0032'),
(33, 'Sharon', 'Green', '2016-07-16', 'Female', '2025-09-01', 2, 'Active', 'sharon.green@example.com', '555-100-0033'),
(34, 'Steven', 'Adams', '2006-10-28', 'Male', '2019-09-01', 12, 'Active', 'steven.adams@example.com', '555-100-0034'),
(35, 'Kathleen', 'Baker', '2017-05-12', 'Female', '2025-08-20', 1, 'Active', 'kathleen.baker@example.com', '555-100-0035'),
(36, 'Jason', 'Nelson', '2011-01-01', 'Male', '2023-08-15', 7, 'Active', 'jason.nelson@example.com', '555-100-0036'),
(37, 'Brenda', 'Carter', '2012-03-29', 'Female', '2023-09-01', 6, 'Active', 'brenda.carter@example.com', '555-100-0037'),
(38, 'Larry', 'Perez', '2010-06-17', 'Male', '2022-09-10', 8, 'Active', 'larry.perez@example.com', '555-100-0038'),
(39, 'Anna', 'Roberts', '2013-08-04', 'Female', '2024-08-25', 5, 'Active', 'anna.roberts@example.com', '555-100-0039'),
(40, 'Justin', 'Turner', '2009-11-12', 'Male', '2021-09-01', 9, 'Active', 'justin.turner@example.com', '555-100-0040'),
(41, 'Cynthia', 'Phillips', '2014-01-23', 'Female', '2024-09-05', 4, 'Active', 'cynthia.phillips@example.com', '555-100-0041'),
(42, 'Raymond', 'Campbell', '2008-02-05', 'Male', '2021-08-10', 10, 'Active', 'raymond.campbell@example.com', '555-100-0042'),
(43, 'Christine', 'Parker', '2015-09-09', 'Female', '2025-08-30', 3, 'Active', 'christine.parker@example.com', '555-100-0043'),
(44, 'Jerry', 'Evans', '2007-07-27', 'Male', '2020-09-05', 11, 'Active', 'jerry.evans@example.com', '555-100-0044'),
(45, 'Pamela', 'Edwards', '2016-02-03', 'Female', '2025-09-10', 2, 'Active', 'pamela.edwards@example.com', '555-100-0045'),
(46, 'Aaron', 'Collins', '2006-08-10', 'Male', '2019-08-20', 12, 'Active', 'aaron.collins@example.com', '555-100-0046'),
(47, 'Evelyn', 'Stewart', '2017-04-01', 'Female', '2025-08-05', 1, 'Active', 'evelyn.stewart@example.com', '555-100-0047'),
(48, 'Scott', 'Sanchez', '2011-09-05', 'Male', '2023-08-25', 7, 'Active', 'scott.sanchez@example.com', '555-100-0048'),
(49, 'Alice', 'Morris', '2012-11-18', 'Female', '2023-09-05', 6, 'Active', 'alice.morris@example.com', '555-100-0049'),
(50, 'Frank', 'Rogers', '2010-01-22', 'Male', '2022-08-10', 8, 'Active', 'frank.rogers@example.com', '555-100-0050'),
(51, 'Martha', 'Reed', '2013-05-30', 'Female', '2024-09-01', 5, 'Active', 'martha.reed@example.com', '555-100-0051'),
(52, 'Gary', 'Cook', '2009-03-11', 'Male', '2021-08-20', 9, 'Active', 'gary.cook@example.com', '555-100-0052'),
(53, 'Joyce', 'Morgan', '2014-06-25', 'Female', '2024-08-10', 4, 'Active', 'joyce.morgan@example.com', '555-100-0053'),
(54, 'Dennis', 'Bell', '2008-01-04', 'Male', '2021-09-05', 10, 'Active', 'dennis.bell@example.com', '555-100-0054'),
(55, 'Victoria', 'Murphy', '2015-07-17', 'Female', '2025-09-01', 3, 'Active', 'victoria.murphy@example.com', '555-100-0055'),
(56, 'Nathan', 'Bailey', '2007-09-08', 'Male', '2020-08-15', 11, 'Active', 'nathan.bailey@example.com', '555-100-0056'),
(57, 'Catherine', 'Rivera', '2016-03-02', 'Female', '2025-08-25', 2, 'Active', 'catherine.rivera@example.com', '555-100-0057'),
(58, 'Walter', 'Cooper', '2006-11-21', 'Male', '2019-09-10', 12, 'Active', 'walter.cooper@example.com', '555-100-0058'),
(59, 'Diane', 'Richardson', '2017-02-06', 'Female', '2025-08-15', 1, 'Active', 'diane.richardson@example.com', '555-100-0059'),
(60, 'Arthur', 'Cox', '2011-04-10', 'Male', '2023-09-10', 7, 'Active', 'arthur.cox@example.com', '555-100-0060'),
(61, 'Julie', 'Howard', '2012-06-14', 'Female', '2023-08-25', 6, 'Active', 'julie.howard@example.com', '555-100-0061'),
(62, 'Zachary', 'Ward', '2010-09-27', 'Male', '2022-09-05', 8, 'Active', 'zachary.ward@example.com', '555-100-0062'),
(63, 'Hannah', 'Torres', '2013-12-08', 'Female', '2024-08-20', 5, 'Active', 'hannah.torres@example.com', '555-100-0063'),
(64, 'Roger', 'Peterson', '2009-02-19', 'Male', '2021-08-15', 9, 'Active', 'roger.peterson@example.com', '555-100-0064'),
(65, 'Debra', 'Gray', '2014-05-01', 'Female', '2024-09-10', 4, 'Active', 'debra.gray@example.com', '555-100-0065'),
(66, 'Randy', 'Ramirez', '2008-10-14', 'Male', '2021-09-01', 10, 'Active', 'randy.ramirez@example.com', '555-100-0066'),
(67, 'Cheryl', 'James', '2015-01-28', 'Female', '2025-08-15', 3, 'Active', 'cheryl.james@example.com', '555-100-0067'),
(68, 'Stephen', 'Watson', '2007-03-06', 'Male', '2020-08-20', 11, 'Active', 'stephen.watson@example.com', '555-100-0068'),
(69, 'Judith', 'Brooks', '2016-08-01', 'Female', '2025-09-05', 2, 'Active', 'judith.brooks@example.com', '555-100-0069'),
(70, 'Joe', 'Kelly', '2006-05-07', 'Male', '2019-08-10', 12, 'Active', 'joe.kelly@example.com', '555-100-0070'),
(71, 'Shirley', 'Sanders', '2017-07-20', 'Female', '2025-08-01', 1, 'Active', 'shirley.sanders@example.com', '555-100-0071'),
(72, 'Jeremy', 'Price', '2011-02-08', 'Male', '2023-09-15', 7, 'Active', 'jeremy.price@example.com', '555-100-0072'),
(73, 'Gloria', 'Bennett', '2012-04-12', 'Female', '2023-08-10', 6, 'Active', 'gloria.bennett@example.com', '555-100-0073'),
(74, 'Harry', 'Wood', '2010-07-03', 'Male', '2022-09-01', 8, 'Active', 'harry.wood@example.com', '555-100-0074'),
(75, 'Teresa', 'Barnes', '2013-10-21', 'Female', '2024-08-25', 5, 'Active', 'teresa.barnes@example.com', '555-100-0075'),
(76, 'Adam', 'Ross', '2009-08-09', 'Male', '2021-08-05', 9, 'Active', 'adam.ross@example.com', '555-100-0076'),
(77, 'Ann', 'Henderson', '2014-11-01', 'Female', '2024-09-01', 4, 'Active', 'ann.henderson@example.com', '555-100-0077'),
(78, 'Fred', 'Coleman', '2008-04-26', 'Male', '2021-09-10', 10, 'Active', 'fred.coleman@example.com', '555-100-0078'),
(79, 'Denise', 'Jenkins', '2015-03-03', 'Female', '2025-08-20', 3, 'Active', 'denise.jenkins@example.com', '555-100-0079'),
(80, 'Randy', 'Perry', '2007-06-18', 'Male', '2020-08-25', 11, 'Active', 'randy.perry@example.com', '555-100-0080'),
(81, 'Paula', 'Powell', '2016-09-02', 'Female', '2025-09-05', 2, 'Active', 'paula.powell@example.com', '555-100-0081'),
(82, 'Billy', 'Long', '2006-02-14', 'Male', '2019-09-01', 12, 'Active', 'billy.long@example.com', '555-100-0082'),
(83, 'Diana', 'Patterson', '2017-06-28', 'Female', '2025-08-10', 1, 'Active', 'diana.patterson@example.com', '555-100-0083'),
(84, 'Lawrence', 'Hughes', '2011-07-19', 'Male', '2023-08-20', 7, 'Active', 'lawrence.hughes@example.com', '555-100-0084'),
(85, 'Louise', 'Flores', '2012-09-01', 'Female', '2023-09-10', 6, 'Active', 'louise.flores@example.com', '555-100-0085'),
(86, 'Dylan', 'Washington', '2010-04-05', 'Male', '2022-08-15', 8, 'Active', 'dylan.washington@example.com', '555-100-0086'),
(87, 'Sara', 'Butler', '2013-06-09', 'Female', '2024-09-05', 5, 'Active', 'sara.butler@example.com', '555-100-0087'),
(88, 'Jesse', 'Simmons', '2009-08-23', 'Male', '2021-08-25', 9, 'Active', 'jesse.simmons@example.com', '555-100-0088'),
(89, 'Rose', 'Foster', '2014-07-16', 'Female', '2024-08-10', 4, 'Active', 'rose.foster@example.com', '555-100-0089'),
(90, 'Phillip', 'Gonzales', '2008-02-02', 'Male', '2021-09-01', 10, 'Active', 'phillip.gonzales@example.com', '555-100-0090'),
(91, 'Helen', 'Bryant', '2015-04-15', 'Female', '2025-09-01', 3, 'Active', 'helen.bryant@example.com', '555-100-0091'),
(92, 'Russell', 'Alexander', '2007-05-28', 'Male', '2020-09-15', 11, 'Active', 'russell.alexander@example.com', '555-100-0092'),
(93, 'Grace', 'Russell', '2016-10-10', 'Female', '2025-08-20', 2, 'Active', 'grace.russell@example.com', '555-100-0093'),
(94, 'Eugene', 'Griffin', '2006-03-01', 'Male', '2019-08-05', 12, 'Active', 'eugene.griffin@example.com', '555-100-0094'),
(95, 'Judy', 'Diaz', '2017-08-24', 'Female', '2025-08-25', 1, 'Active', 'judy.diaz@example.com', '555-100-0095'),
(96, 'Howard', 'Hayes', '2011-12-07', 'Male', '2023-09-01', 7, 'Active', 'howard.hayes@example.com', '555-100-0096'),
(97, 'Marilyn', 'Myers', '2012-02-18', 'Female', '2023-08-15', 6, 'Active', 'marilyn.myers@example.com', '555-100-0097'),
(98, 'Vincent', 'Ford', '2010-05-22', 'Male', '2022-09-10', 8, 'Active', 'vincent.ford@example.com', '555-100-0098'),
(99, 'Heather', 'Hamilton', '2013-07-06', 'Female', '2024-08-20', 5, 'Active', 'heather.hamilton@example.com', '555-100-0099'),
(100, 'Todd', 'Graham', '2009-10-25', 'Male', '2021-08-25', 9, 'Active', 'todd.graham@example.com', '555-100-0100'),
(101, 'Kelly', 'Sullivan', '2014-12-09', 'Female', '2024-09-01', 4, 'Active', 'kelly.sullivan@example.com', '555-100-0101'),
(102, 'Russell', 'Wallace', '2008-05-16', 'Male', '2021-09-05', 10, 'Active', 'russell.wallace@example.com', '555-100-0102'),
(103, 'Christina', 'Woods', '2015-08-01', 'Female', '2025-08-10', 3, 'Active', 'christina.woods@example.com', '555-100-0103'),
(104, 'Bobby', 'Cole', '2007-01-20', 'Male', '2020-09-01', 11, 'Active', 'bobby.cole@example.com', '555-100-0104'),
(105, 'Janet', 'West', '2016-06-13', 'Female', '2025-09-10', 2, 'Active', 'janet.west@example.com', '555-100-0105'),
(106, 'Johnny', 'Jordan', '2006-09-28', 'Male', '2019-08-25', 12, 'Active', 'johnny.jordan@example.com', '555-100-0106'),
(107, 'Brenda', 'Fisher', '2017-03-05', 'Female', '2025-08-05', 1, 'Active', 'brenda.fisher@example.com', '555-100-0107'),
(108, 'Jeffrey', 'Owens', '2011-05-18', 'Male', '2023-08-10', 7, 'Active', 'jeffrey.owens@example.com', '555-100-0108'),
(109, 'Kathy', 'Harrison', '2012-07-22', 'Female', '2023-09-05', 6, 'Active', 'kathy.harrison@example.com', '555-100-0109'),
(110, 'Jesse', 'Kennedy', '2010-10-03', 'Male', '2022-08-15', 8, 'Active', 'jesse.kennedy@example.com', '555-100-0110'),
(111, 'Virginia', 'Moore', '2013-01-16', 'Female', '2024-09-01', 5, 'Active', 'virginia.moore@example.com', '555-100-0111'),
(112, 'Kevin', 'Peters', '2009-04-08', 'Male', '2021-08-20', 9, 'Active', 'kevin.peters@example.com', '555-100-0112'),
(113, 'Christine', 'Myers', '2014-06-21', 'Female', '2024-08-10', 4, 'Active', 'christine.myers@example.com', '555-100-0113'),
(114, 'Frank', 'Diaz', '2008-08-03', 'Male', '2021-09-01', 10, 'Active', 'frank.diaz@example.com', '555-100-0114'),
(115, 'Marie', 'Hayes', '2015-09-15', 'Female', '2025-09-01', 3, 'Active', 'marie.hayes@example.com', '555-100-0115'),
(116, 'Jeremy', 'Ford', '2007-12-28', 'Male', '2020-08-15', 11, 'Active', 'jeremy.ford@example.com', '555-100-0116'),
(117, 'Doris', 'Graham', '2016-05-10', 'Female', '2025-08-25', 2, 'Active', 'doris.graham@example.com', '555-100-0117'),
(118, 'Billy', 'Sullivan', '2006-07-24', 'Male', '2019-09-10', 12, 'Active', 'billy.sullivan@example.com', '555-100-0118'),
(119, 'Mildred', 'Wallace', '2017-10-06', 'Female', '2025-08-15', 1, 'Active', 'mildred.wallace@example.com', '555-100-0119'),
(120, 'Roger', 'Woods', '2011-01-19', 'Male', '2023-09-10', 7, 'Active', 'roger.woods@example.com', '555-100-0120'),
(121, 'Theresa', 'Cole', '2012-03-03', 'Female', '2023-08-25', 6, 'Active', 'theresa.cole@example.com', '555-100-0121'),
(122, 'Joseph', 'West', '2010-06-16', 'Male', '2022-09-05', 8, 'Active', 'joseph.west@example.com', '555-100-0122'),
(123, 'Beverly', 'Jordan', '2013-09-29', 'Female', '2024-08-20', 5, 'Active', 'beverly.jordan@example.com', '555-100-0123'),
(124, 'Adam', 'Fisher', '2009-02-10', 'Male', '2021-08-15', 9, 'Active', 'adam.fisher@example.com', '555-100-0124'),
(125, 'Frances', 'Owens', '2014-04-24', 'Female', '2024-09-10', 4, 'Active', 'frances.owens@example.com', '555-100-0125'),
(126, 'Samuel', 'Harrison', '2008-07-07', 'Male', '2021-09-01', 10, 'Active', 'samuel.harrison@example.com', '555-100-0126'),
(127, 'Louise', 'Kennedy', '2015-10-20', 'Female', '2025-08-15', 3, 'Active', 'louise.kennedy@example.com', '555-100-0127'),
(128, 'Henry', 'Moore', '2007-01-01', 'Male', '2020-08-20', 11, 'Active', 'henry.moore@example.com', '555-100-0128'),
(129, 'Alice', 'Peters', '2016-06-13', 'Female', '2025-09-05', 2, 'Active', 'alice.peters@example.com', '555-100-0129'),
(130, 'Jack', 'Myers', '2006-09-26', 'Male', '2019-08-10', 12, 'Active', 'jack.myers@example.com', '555-100-0130'),
(131, 'Linda', 'Diaz', '2017-02-09', 'Female', '2025-08-01', 1, 'Active', 'linda.diaz@example.com', '555-100-0131'),
(132, 'Peter', 'Hayes', '2011-04-03', 'Male', '2023-09-01', 7, 'Active', 'peter.hayes@example.com', '555-100-0132'),
(133, 'Megan', 'Ford', '2012-05-17', 'Female', '2023-08-15', 6, 'Active', 'megan.ford@example.com', '555-100-0133'),
(134, 'Patrick', 'Graham', '2010-08-30', 'Male', '2022-09-10', 8, 'Active', 'patrick.graham@example.com', '555-100-0134'),
(135, 'Olivia', 'Sullivan', '2013-11-13', 'Female', '2024-08-20', 5, 'Active', 'olivia.sullivan@example.com', '555-100-0135'),
(136, 'Paul', 'Wallace', '2009-03-26', 'Male', '2021-08-25', 9, 'Active', 'paul.wallace@example.com', '555-100-0136'),
(137, 'Julia', 'Woods', '2014-05-09', 'Female', '2024-09-01', 4, 'Active', 'julia.woods@example.com', '555-100-0137'),
(138, 'Steven', 'Cole', '2008-07-22', 'Male', '2021-09-05', 10, 'Active', 'steven.cole@example.com', '555-100-0138'),
(139, 'Ashley', 'West', '2015-09-04', 'Female', '2025-08-10', 3, 'Active', 'ashley.west@example.com', '555-100-0139'),
(140, 'Kevin', 'Jordan', '2007-12-17', 'Male', '2020-09-01', 11, 'Active', 'kevin.jordan@example.com', '555-100-0140'),
(141, 'Christina', 'Fisher', '2016-02-29', 'Female', '2025-09-10', 2, 'Active', 'christina.fisher@example.com', '555-100-0141'),
(142, 'Ronald', 'Owens', '2006-05-14', 'Male', '2019-08-25', 12, 'Active', 'ronald.owens@example.com', '555-100-0142'),
(143, 'Shirley', 'Harrison', '2017-08-27', 'Female', '2025-08-05', 1, 'Active', 'shirley.harrison@example.com', '555-100-0143'),
(144, 'Donald', 'Kennedy', '2011-10-09', 'Male', '2023-08-10', 7, 'Active', 'donald.kennedy@example.com', '555-100-0144'),
(145, 'Amy', 'Moore', '2012-12-03', 'Female', '2023-09-05', 6, 'Active', 'amy.moore@example.com', '555-100-0145'),
(146, 'Raymond', 'Peters', '2010-02-15', 'Male', '2022-08-15', 8, 'Active', 'raymond.peters@example.com', '555-100-0146'),
(147, 'Victoria', 'Myers', '2013-04-28', 'Female', '2024-09-01', 5, 'Active', 'victoria.myers@example.com', '555-100-0147'),
(148, 'Arthur', 'Diaz', '2009-06-11', 'Male', '2021-08-20', 9, 'Active', 'arthur.diaz@example.com', '555-100-0148'),
(149, 'Gloria', 'Hayes', '2014-08-24', 'Female', '2024-08-10', 4, 'Active', 'gloria.hayes@example.com', '555-100-0149'),
(150, 'Philip', 'Ford', '2008-10-07', 'Male', '2021-09-01', 10, 'Active', 'philip.ford@example.com', '555-100-0150'),
(151, 'Laura', 'Graham', '2015-12-20', 'Female', '2025-09-01', 3, 'Active', 'laura.graham@example.com', '555-100-0151'),
(152, 'Walter', 'Sullivan', '2007-02-01', 'Male', '2020-08-15', 11, 'Active', 'walter.sullivan@example.com', '555-100-0152'),
(153, 'Pamela', 'Wallace', '2016-04-14', 'Female', '2025-08-25', 2, 'Active', 'pamela.wallace@example.com', '555-100-0153'),
(154, 'Patrick', 'Woods', '2006-06-27', 'Male', '2019-09-10', 12, 'Active', 'patrick.woods@example.com', '555-100-0154'),
(155, 'Kathleen', 'Cole', '2017-09-09', 'Female', '2025-08-15', 1, 'Active', 'kathleen.cole@example.com', '555-100-0155'),
(156, 'Dennis', 'West', '2011-11-22', 'Male', '2023-09-10', 7, 'Active', 'dennis.west@example.com', '555-100-0156'),
(157, 'Sharon', 'Jordan', '2012-01-05', 'Female', '2023-08-25', 6, 'Active', 'sharon.jordan@example.com', '555-100-0157'),
(158, 'Gary', 'Fisher', '2010-03-18', 'Male', '2022-09-05', 8, 'Active', 'gary.fisher@example.com', '555-100-0158'),
(159, 'Judy', 'Owens', '2013-05-31', 'Female', '2024-08-20', 5, 'Active', 'judy.owens@example.com', '555-100-0159'),
(160, 'George', 'Harrison', '2009-07-14', 'Male', '2021-08-15', 9, 'Active', 'george.harrison@example.com', '555-100-0160'),
(161, 'Julia', 'Kennedy', '2014-09-27', 'Female', '2024-09-10', 4, 'Active', 'julia.kennedy@example.com', '555-100-0161'),
(162, 'Roy', 'Moore', '2008-11-10', 'Male', '2021-09-01', 10, 'Active', 'roy.moore@example.com', '555-100-0162'),
(163, 'Amanda', 'Peters', '2015-01-23', 'Female', '2025-08-15', 3, 'Active', 'amanda.peters@example.com', '555-100-0163'),
(164, 'Willie', 'Myers', '2007-03-08', 'Male', '2020-08-20', 11, 'Active', 'willie.myers@example.com', '555-100-0164'),
(165, 'Rebecca', 'Diaz', '2016-08-21', 'Female', '2025-09-05', 2, 'Active', 'rebecca.diaz@example.com', '555-100-0165'),
(166, 'Jerry', 'Hayes', '2006-10-04', 'Male', '2019-08-10', 12, 'Active', 'jerry.hayes@example.com', '555-100-0166'),
(167, 'Karen', 'Ford', '2017-12-17', 'Female', '2025-08-01', 1, 'Active', 'karen.ford@example.com', '555-100-0167'),
(168, 'Harry', 'Graham', '2011-02-01', 'Male', '2023-09-01', 7, 'Active', 'harry.graham@example.com', '555-100-0168'),
(169, 'Dorothy', 'Sullivan', '2012-04-15', 'Female', '2023-08-15', 6, 'Active', 'dorothy.sullivan@example.com', '555-100-0169');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Students`
--
ALTER TABLE `Students`
  ADD PRIMARY KEY (`student_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Students`
--
ALTER TABLE `Students`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=170;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
