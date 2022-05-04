-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: zzz_xxxxx_NOM_PRENOM_INFO1X_SUJET_104_2021

-- Détection si une autre base de donnée du même nom existe

DROP DATABASE IF EXISTS Lopardo_Mattia_INFO1C_164_BD;

CREATE DATABASE IF NOT EXISTS Lopardo_Mattia_INFO1C_164_BD;

USE Lopardo_Mattia_INFO1C_164_BD;


-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mar 05 Avril 2022 à 14:33
-- Version du serveur :  5.7.11
-- Version de PHP :  5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `lopardo_mattia_info1c_164_bd`
--

-- --------------------------------------------------------

--
-- Structure de la table `adresse`
--

CREATE TABLE `adresse` (
  `id_adresse` int(11) NOT NULL,
  `adresse` varchar(50) DEFAULT NULL,
  `NPA` int(25) DEFAULT NULL,
  `ville` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `adresse`
--

INSERT INTO `adresse` (`id_adresse`, `adresse`, `NPA`, `ville`) VALUES
(1, 'Via Altisio 36', 1688, 'Sommentier'),
(2, 'Via Schliffras 98', 5637, 'Geltwil'),
(3, 'Via Franscini 6', 9327, 'Tübach'),
(4, 'Via Camischolas sura 4', 3036, 'Detligen'),
(5, 'Grossmatt 100', 8242, 'Bibern'),
(6, 'Via Gabbietta 29', 6653, 'Verscio'),
(7, 'Betburweg 128', 7058, 'Litzirüti'),
(8, 'Brunnacherstrasse 71', 3303, 'Zuzwil'),
(9, 'Fortunastrasse 81', 3423, 'Ersigen'),
(10, 'Valéestrasse 100', 1413, 'Oppens'),
(11, ' Grossmatt 113', 9248, 'Bichwil'),
(12, 'Erlenweg 25', 5636, 'Benzenschwil'),
(13, 'Stradun 133', 1523, 'Granges-près-marnand'),
(14, ' Kornquaderweg 102', 6432, 'Rickenbach'),
(15, 'Höhenweg 110', 4558, 'Heinrichswil'),
(16, ' Üerklisweg 29', 6827, 'Brusino Arsizio'),
(17, 'Im Sandbüel 85', 2027, ' Fresens');

-- --------------------------------------------------------

--
-- Structure de la table `categorie`
--

CREATE TABLE `categorie` (
  `id_categorie` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `categorie`
--

INSERT INTO `categorie` (`id_categorie`) VALUES
('bénéficiaire'),
('technicien');

-- --------------------------------------------------------

--
-- Structure de la table `demande`
--

CREATE TABLE `demande` (
  `id_demande` int(11) NOT NULL,
  `nom_demande` varchar(40) DEFAULT NULL,
  `numero_demande` int(11) NOT NULL,
  `description_demande` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `demande`
--

INSERT INTO `demande` (`id_demande`, `nom_demande`, `numero_demande`, `description_demande`) VALUES
(1, 'nouveau laptop', 9983525, 'Le bénéficiare aimerait un nouveau laptop pour travailler correctement'),
(2, 'nouvelle docking', 9924323, 'Le bénéficiare aimerait une nouvelle docking pour travailler correctement'),
(3, 'nouvelle souris', 9892444, 'Le bénéficiare aimerait une nouvelle souris pour travailler correctement'),
(4, 'nouveau clavier', 9821467, 'Le bénéficiare aimerait un nouveau clavier pour travailler correctement'),
(5, 'nouveau écran', 9977668, 'Le bénéficiare aimerait un nouveau écran pour travailler correctement');

-- --------------------------------------------------------

--
-- Structure de la table `departement`
--

CREATE TABLE `departement` (
  `id_departement` int(11) NOT NULL,
  `nom_departement` varchar(50) DEFAULT NULL,
  `num_departement` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `departement`
--

INSERT INTO `departement` (`id_departement`, `nom_departement`, `num_departement`) VALUES
(1, 'institutions et\r\ndu territoire\r\nDIT', 1),
(2, 'formation, de la jeunesse\r\n et de la culture\r\nDFJC', 2),
(3, 'l’environnement\r\net de la sécurité\r\nDES', 3),
(4, 'santé et\r\nde l’action sociale\r\nDSAS', 4),
(5, 'l’économie, de\r\nl’innovation et du sport\r\nDEIS', 5),
(6, 'infrastructures et des\r\n ressources humaines\r\nDIRH', 6),
(7, 'finances et des relations\r\nextérieures\r\nDFIRE', 7);

-- --------------------------------------------------------

--
-- Structure de la table `dep_avoir_mail`
--

CREATE TABLE `dep_avoir_mail` (
  `id_dep_avoir_mail` int(11) NOT NULL,
  `FK_departement` int(11) NOT NULL,
  `FK_mail` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `dep_avoir_mail`
--

INSERT INTO `dep_avoir_mail` (`id_dep_avoir_mail`, `FK_departement`, `FK_mail`) VALUES
(1, 1, 11),
(2, 2, 12),
(3, 3, 13),
(4, 4, 14),
(5, 5, 16),
(6, 6, 15),
(7, 7, 17);

-- --------------------------------------------------------

--
-- Structure de la table `dep_avoir_tel`
--

CREATE TABLE `dep_avoir_tel` (
  `id_dep_avoir_tel` int(11) NOT NULL,
  `FK_departement` int(11) NOT NULL,
  `FK_telephone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `dep_avoir_tel`
--

INSERT INTO `dep_avoir_tel` (`id_dep_avoir_tel`, `FK_departement`, `FK_telephone`) VALUES
(1, 1, 11),
(2, 2, 12),
(3, 3, 13),
(4, 4, 14),
(5, 5, 15),
(6, 6, 16),
(7, 7, 17);

-- --------------------------------------------------------

--
-- Structure de la table `dep_se_trouver_adresse`
--

CREATE TABLE `dep_se_trouver_adresse` (
  `id_dep_se_trouver_adresse` int(11) NOT NULL,
  `FK_departement` int(11) NOT NULL,
  `FK_adresse` int(11) NOT NULL,
  `date_adresse` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `dep_se_trouver_adresse`
--

INSERT INTO `dep_se_trouver_adresse` (`id_dep_se_trouver_adresse`, `FK_departement`, `FK_adresse`, `date_adresse`) VALUES
(1, 1, 11, '2022-04-05'),
(2, 2, 12, '2022-04-05'),
(3, 3, 13, '2022-04-05'),
(4, 4, 14, '2022-04-05'),
(5, 5, 15, '2022-04-05'),
(6, 6, 16, '2022-04-05'),
(7, 7, 17, '2022-04-05');

-- --------------------------------------------------------

--
-- Structure de la table `incident`
--

CREATE TABLE `incident` (
  `id_incident` int(11) NOT NULL,
  `nom_incident` varchar(40) DEFAULT NULL,
  `numero_incident` int(11) NOT NULL,
  `description_incident` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `incident`
--

INSERT INTO `incident` (`id_incident`, `nom_incident`, `numero_incident`, `description_incident`) VALUES
(1, 'laptop cassé', 9738754, 'Le bénéficiaire à besoin d\'un nouveau laptop au plus vite'),
(2, 'écran fissuré', 9718634, 'Le bénéficiaire à besoin d\'un nouveau écran au plus vite');

-- --------------------------------------------------------

--
-- Structure de la table `mail`
--

CREATE TABLE `mail` (
  `id_mail` int(11) NOT NULL,
  `nom_mail` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `mail`
--

INSERT INTO `mail` (`id_mail`, `nom_mail`) VALUES
(1, 'DupondPierre@eduvaud.vd'),
(2, 'WatsonMarie@eduvaud.vd'),
(3, 'pattinsonpeter@eduvaud.vd'),
(4, 'colehayden@eduvaud.vd'),
(5, 'briantjefferson@eduvaud.vd'),
(6, 'kobeanderson@eduvaud.vd'),
(7, 'JamesKarl@eduvaud.vd'),
(8, 'MoralesMiles@eduvaud.vd'),
(9, 'Pettersonkild@eduvaud.vd'),
(10, 'DwaneyDavide@eduvaud.vd'),
(11, 'DIT@eduvaud.vd'),
(12, 'DFJC@eduvaud.vd'),
(13, 'DES@eduvaud.vd'),
(14, 'DSAS@eduvaud.vd'),
(15, 'DIRH@eduvaud.vd'),
(16, 'DEIS@eduvaud.vd'),
(17, 'DFIRE@eduvaud.vd');

-- --------------------------------------------------------

--
-- Structure de la table `personne`
--

CREATE TABLE `personne` (
  `id_personne` int(11) NOT NULL,
  `nom_personne` varchar(30) DEFAULT NULL,
  `prenom_personne` varchar(30) DEFAULT NULL,
  `date_naiss_personne` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `personne`
--

INSERT INTO `personne` (`id_personne`, `nom_personne`, `prenom_personne`, `date_naiss_personne`) VALUES
(1, 'Dupond', 'Pierre', '1994-08-10'),
(2, 'Watson', 'Marie', '1993-10-12'),
(3, 'pattinson', 'peter', '1980-01-09'),
(4, 'cole', 'hayden', '1995-02-22'),
(5, 'briant', 'jefferson', '2000-11-15'),
(6, 'kobe', 'anderson', '2003-12-11'),
(7, 'James', 'Karl', '2001-03-29'),
(8, 'Morales', 'Miles', '2001-06-20'),
(9, 'Petterson', 'kild', '2002-07-23'),
(10, 'Dwaney', 'Davide', '1985-04-27');

-- --------------------------------------------------------

--
-- Structure de la table `pers_attribuer_dem`
--

CREATE TABLE `pers_attribuer_dem` (
  `id_pers_attribuer_dem` int(11) NOT NULL,
  `FK_personne` int(11) NOT NULL,
  `FK_demande` int(11) NOT NULL,
  `date_attribution` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pers_attribuer_dem`
--

INSERT INTO `pers_attribuer_dem` (`id_pers_attribuer_dem`, `FK_personne`, `FK_demande`, `date_attribution`) VALUES
(1, 5, 1, '2022-04-05'),
(2, 6, 2, '2022-04-05'),
(3, 7, 3, '2022-04-05'),
(4, 8, 4, '2022-04-05'),
(5, 9, 5, '2022-04-05');

-- --------------------------------------------------------

--
-- Structure de la table `pers_attribuer_inc`
--

CREATE TABLE `pers_attribuer_inc` (
  `id_pers_attribuer_inc` int(11) NOT NULL,
  `FK_personne` int(11) NOT NULL,
  `Fk_incident` int(11) NOT NULL,
  `date_attribution` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pers_attribuer_inc`
--

INSERT INTO `pers_attribuer_inc` (`id_pers_attribuer_inc`, `FK_personne`, `Fk_incident`, `date_attribution`) VALUES
(1, 10, 1, '2022-04-05'),
(2, 6, 2, '2022-04-05');

-- --------------------------------------------------------

--
-- Structure de la table `pers_auteur_dem`
--

CREATE TABLE `pers_auteur_dem` (
  `id_pers_auteur_dem` int(11) NOT NULL,
  `FK_personne` int(11) NOT NULL,
  `FK_demande` int(11) NOT NULL,
  `date_crea_dem` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pers_auteur_dem`
--

INSERT INTO `pers_auteur_dem` (`id_pers_auteur_dem`, `FK_personne`, `FK_demande`, `date_crea_dem`) VALUES
(1, 1, 1, '2022-04-05'),
(2, 2, 2, '2022-04-05'),
(3, 1, 3, '2022-04-05'),
(4, 2, 4, '2022-04-05'),
(5, 1, 5, '2022-04-05');

-- --------------------------------------------------------

--
-- Structure de la table `pers_auteur_inc`
--

CREATE TABLE `pers_auteur_inc` (
  `id_pers_auteur_inc` int(11) NOT NULL,
  `FK_personne` int(11) NOT NULL,
  `FK_incident` int(11) NOT NULL,
  `date_crea_inc` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pers_auteur_inc`
--

INSERT INTO `pers_auteur_inc` (`id_pers_auteur_inc`, `FK_personne`, `FK_incident`, `date_crea_inc`) VALUES
(1, 3, 1, '2022-04-05'),
(2, 4, 2, '2022-04-05');

-- --------------------------------------------------------

--
-- Structure de la table `pers_avoir_mail`
--

CREATE TABLE `pers_avoir_mail` (
  `id_pers_avoir_mail` int(11) NOT NULL,
  `FK_personne` int(11) NOT NULL,
  `FK_mail` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pers_avoir_mail`
--

INSERT INTO `pers_avoir_mail` (`id_pers_avoir_mail`, `FK_personne`, `FK_mail`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

-- --------------------------------------------------------

--
-- Structure de la table `pers_avoir_tel`
--

CREATE TABLE `pers_avoir_tel` (
  `id_pers_avoir_tel` int(11) NOT NULL,
  `FK_personne` int(11) NOT NULL,
  `FK_telephone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pers_avoir_tel`
--

INSERT INTO `pers_avoir_tel` (`id_pers_avoir_tel`, `FK_personne`, `FK_telephone`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

-- --------------------------------------------------------

--
-- Structure de la table `pers_categorie`
--

CREATE TABLE `pers_categorie` (
  `id_pers_categorie` int(11) NOT NULL,
  `FK_personne` int(11) NOT NULL,
  `FK_categorie` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pers_categorie`
--

INSERT INTO `pers_categorie` (`id_pers_categorie`, `FK_personne`, `FK_categorie`) VALUES
(1, 1, 'bénéficiaire'),
(2, 2, 'bénéficiaire'),
(3, 3, 'bénéficiaire'),
(4, 4, 'bénéficiaire'),
(5, 5, 'technicien'),
(6, 6, 'technicien'),
(7, 7, 'technicien'),
(8, 8, 'technicien'),
(9, 9, 'technicien'),
(10, 10, 'technicien');

-- --------------------------------------------------------

--
-- Structure de la table `pers_se_trouver_adresse`
--

CREATE TABLE `pers_se_trouver_adresse` (
  `id_pers_se_trouver_adresse` int(11) NOT NULL,
  `FK_personne` int(11) NOT NULL,
  `FK_adresse` int(11) NOT NULL,
  `date_adresse` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pers_se_trouver_adresse`
--

INSERT INTO `pers_se_trouver_adresse` (`id_pers_se_trouver_adresse`, `FK_personne`, `FK_adresse`, `date_adresse`) VALUES
(1, 1, 1, '2022-04-05'),
(2, 2, 2, '2022-04-05'),
(3, 3, 3, '2022-04-05'),
(4, 4, 4, '2022-04-05'),
(5, 5, 5, '2022-04-05'),
(6, 6, 6, '2022-04-05'),
(7, 7, 7, '2022-04-05'),
(8, 8, 8, '2022-04-05'),
(9, 9, 9, '2022-04-05'),
(10, 10, 10, '2022-04-05');

-- --------------------------------------------------------

--
-- Structure de la table `pers_travailler_dep`
--

CREATE TABLE `pers_travailler_dep` (
  `id_pers_travailler_dep` int(11) NOT NULL,
  `FK_personne` int(11) DEFAULT NULL,
  `FK_departement` int(11) DEFAULT NULL,
  `date_debut` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pers_travailler_dep`
--

INSERT INTO `pers_travailler_dep` (`id_pers_travailler_dep`, `FK_personne`, `FK_departement`, `date_debut`) VALUES
(1, 1, 3, '2022-04-05'),
(2, 2, 1, '2022-04-05'),
(3, 3, 2, '2022-04-05'),
(4, 4, 5, '2022-04-05'),
(5, 5, 4, '2022-04-05'),
(6, 6, 7, '2022-04-05'),
(7, 7, 6, '2022-04-05'),
(8, 8, 5, '2022-04-05'),
(9, 9, 6, '2022-04-05'),
(10, 10, 4, '2022-04-05');

-- --------------------------------------------------------

--
-- Structure de la table `telephone`
--

CREATE TABLE `telephone` (
  `id_telephone` int(11) NOT NULL,
  `num_telephone` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `telephone`
--

INSERT INTO `telephone` (`id_telephone`, `num_telephone`) VALUES
(1, 796544323),
(2, 795436787),
(3, 793458745),
(4, 796557623),
(5, 798775643),
(6, 794365489),
(7, 796346576),
(8, 798765684),
(9, 792769823),
(10, 798348629),
(11, 217459539),
(12, 218743891),
(13, 219457218),
(14, 216783593),
(15, 213847238),
(16, 218598724),
(17, 219347538);

--
-- Index pour les tables exportées
--

--
-- Index pour la table `adresse`
--
ALTER TABLE `adresse`
  ADD PRIMARY KEY (`id_adresse`);

--
-- Index pour la table `categorie`
--
ALTER TABLE `categorie`
  ADD PRIMARY KEY (`id_categorie`);

--
-- Index pour la table `demande`
--
ALTER TABLE `demande`
  ADD PRIMARY KEY (`id_demande`);

--
-- Index pour la table `departement`
--
ALTER TABLE `departement`
  ADD PRIMARY KEY (`id_departement`);

--
-- Index pour la table `dep_avoir_mail`
--
ALTER TABLE `dep_avoir_mail`
  ADD PRIMARY KEY (`id_dep_avoir_mail`),
  ADD KEY `FKmail_dep` (`FK_departement`),
  ADD KEY `FKmail_dep_mail` (`FK_mail`);

--
-- Index pour la table `dep_avoir_tel`
--
ALTER TABLE `dep_avoir_tel`
  ADD PRIMARY KEY (`id_dep_avoir_tel`),
  ADD KEY `FKtelephone_dep` (`FK_departement`),
  ADD KEY `FKtelephone_dep_tel` (`FK_telephone`);

--
-- Index pour la table `dep_se_trouver_adresse`
--
ALTER TABLE `dep_se_trouver_adresse`
  ADD PRIMARY KEY (`id_dep_se_trouver_adresse`),
  ADD KEY `FKadresse_dep` (`FK_departement`),
  ADD KEY `FKadresse_dep_adresse` (`FK_adresse`);

--
-- Index pour la table `incident`
--
ALTER TABLE `incident`
  ADD PRIMARY KEY (`id_incident`);

--
-- Index pour la table `mail`
--
ALTER TABLE `mail`
  ADD PRIMARY KEY (`id_mail`);

--
-- Index pour la table `personne`
--
ALTER TABLE `personne`
  ADD PRIMARY KEY (`id_personne`);

--
-- Index pour la table `pers_attribuer_dem`
--
ALTER TABLE `pers_attribuer_dem`
  ADD PRIMARY KEY (`id_pers_attribuer_dem`),
  ADD KEY `FKpersonne_attr_dem` (`FK_personne`),
  ADD KEY `FKdem_attr` (`FK_demande`);

--
-- Index pour la table `pers_attribuer_inc`
--
ALTER TABLE `pers_attribuer_inc`
  ADD PRIMARY KEY (`id_pers_attribuer_inc`),
  ADD KEY `FKinc_attr_inc` (`Fk_incident`),
  ADD KEY `FKinc_attr_pers` (`FK_personne`);

--
-- Index pour la table `pers_auteur_dem`
--
ALTER TABLE `pers_auteur_dem`
  ADD PRIMARY KEY (`id_pers_auteur_dem`),
  ADD KEY `FKdem_auteur` (`FK_demande`),
  ADD KEY `FKdem_auteur_pers` (`FK_personne`);

--
-- Index pour la table `pers_auteur_inc`
--
ALTER TABLE `pers_auteur_inc`
  ADD PRIMARY KEY (`id_pers_auteur_inc`),
  ADD KEY `FKinc_auteur_pers` (`FK_personne`),
  ADD KEY `FKinc_auteur_inc` (`FK_incident`);

--
-- Index pour la table `pers_avoir_mail`
--
ALTER TABLE `pers_avoir_mail`
  ADD PRIMARY KEY (`id_pers_avoir_mail`),
  ADD KEY `FKmail_pers` (`FK_personne`),
  ADD KEY `FKmail_pers_mail` (`FK_mail`);

--
-- Index pour la table `pers_avoir_tel`
--
ALTER TABLE `pers_avoir_tel`
  ADD PRIMARY KEY (`id_pers_avoir_tel`),
  ADD KEY `FKtelephone_pers` (`FK_telephone`),
  ADD KEY `FKtelephone_pers_pers` (`FK_personne`);

--
-- Index pour la table `pers_categorie`
--
ALTER TABLE `pers_categorie`
  ADD PRIMARY KEY (`id_pers_categorie`),
  ADD KEY `FKpersonne` (`FK_personne`),
  ADD KEY `FKcategorie` (`FK_categorie`);

--
-- Index pour la table `pers_se_trouver_adresse`
--
ALTER TABLE `pers_se_trouver_adresse`
  ADD PRIMARY KEY (`id_pers_se_trouver_adresse`),
  ADD KEY `FKpersonne_adresse` (`FK_personne`),
  ADD KEY `FKadresse_adresse` (`FK_adresse`);

--
-- Index pour la table `pers_travailler_dep`
--
ALTER TABLE `pers_travailler_dep`
  ADD PRIMARY KEY (`id_pers_travailler_dep`),
  ADD KEY `FKpers_travailler_dep` (`FK_departement`),
  ADD KEY `FKpers_travailler_dep_pers` (`FK_personne`);

--
-- Index pour la table `telephone`
--
ALTER TABLE `telephone`
  ADD PRIMARY KEY (`id_telephone`);

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `dep_avoir_mail`
--
ALTER TABLE `dep_avoir_mail`
  ADD CONSTRAINT `FKmail_dep` FOREIGN KEY (`FK_departement`) REFERENCES `departement` (`id_departement`),
  ADD CONSTRAINT `FKmail_dep_mail` FOREIGN KEY (`FK_mail`) REFERENCES `mail` (`id_mail`);

--
-- Contraintes pour la table `dep_avoir_tel`
--
ALTER TABLE `dep_avoir_tel`
  ADD CONSTRAINT `FKtelephone_dep` FOREIGN KEY (`FK_departement`) REFERENCES `departement` (`id_departement`),
  ADD CONSTRAINT `FKtelephone_dep_tel` FOREIGN KEY (`FK_telephone`) REFERENCES `telephone` (`id_telephone`);

--
-- Contraintes pour la table `dep_se_trouver_adresse`
--
ALTER TABLE `dep_se_trouver_adresse`
  ADD CONSTRAINT `FKadresse_dep` FOREIGN KEY (`FK_departement`) REFERENCES `departement` (`id_departement`),
  ADD CONSTRAINT `FKadresse_dep_adresse` FOREIGN KEY (`FK_adresse`) REFERENCES `adresse` (`id_adresse`);

--
-- Contraintes pour la table `pers_attribuer_dem`
--
ALTER TABLE `pers_attribuer_dem`
  ADD CONSTRAINT `FKdem_attr` FOREIGN KEY (`FK_demande`) REFERENCES `demande` (`id_demande`),
  ADD CONSTRAINT `FKpersonne_attr_dem` FOREIGN KEY (`FK_personne`) REFERENCES `personne` (`id_personne`);

--
-- Contraintes pour la table `pers_attribuer_inc`
--
ALTER TABLE `pers_attribuer_inc`
  ADD CONSTRAINT `FKinc_attr_inc` FOREIGN KEY (`Fk_incident`) REFERENCES `incident` (`id_incident`),
  ADD CONSTRAINT `FKinc_attr_pers` FOREIGN KEY (`FK_personne`) REFERENCES `personne` (`id_personne`);

--
-- Contraintes pour la table `pers_auteur_dem`
--
ALTER TABLE `pers_auteur_dem`
  ADD CONSTRAINT `FKdem_auteur` FOREIGN KEY (`FK_demande`) REFERENCES `demande` (`id_demande`),
  ADD CONSTRAINT `FKdem_auteur_pers` FOREIGN KEY (`FK_personne`) REFERENCES `personne` (`id_personne`);

--
-- Contraintes pour la table `pers_auteur_inc`
--
ALTER TABLE `pers_auteur_inc`
  ADD CONSTRAINT `FKinc_auteur_inc` FOREIGN KEY (`FK_incident`) REFERENCES `incident` (`id_incident`),
  ADD CONSTRAINT `FKinc_auteur_pers` FOREIGN KEY (`FK_personne`) REFERENCES `personne` (`id_personne`);

--
-- Contraintes pour la table `pers_avoir_mail`
--
ALTER TABLE `pers_avoir_mail`
  ADD CONSTRAINT `FKmail_pers` FOREIGN KEY (`FK_personne`) REFERENCES `personne` (`id_personne`),
  ADD CONSTRAINT `FKmail_pers_mail` FOREIGN KEY (`FK_mail`) REFERENCES `mail` (`id_mail`);

--
-- Contraintes pour la table `pers_avoir_tel`
--
ALTER TABLE `pers_avoir_tel`
  ADD CONSTRAINT `FKtelephone_pers` FOREIGN KEY (`FK_telephone`) REFERENCES `telephone` (`id_telephone`),
  ADD CONSTRAINT `FKtelephone_pers_pers` FOREIGN KEY (`FK_personne`) REFERENCES `personne` (`id_personne`);

--
-- Contraintes pour la table `pers_categorie`
--
ALTER TABLE `pers_categorie`
  ADD CONSTRAINT `FKcategorie` FOREIGN KEY (`FK_categorie`) REFERENCES `categorie` (`id_categorie`),
  ADD CONSTRAINT `FKpersonne` FOREIGN KEY (`FK_personne`) REFERENCES `personne` (`id_personne`);

--
-- Contraintes pour la table `pers_se_trouver_adresse`
--
ALTER TABLE `pers_se_trouver_adresse`
  ADD CONSTRAINT `FKadresse_adresse` FOREIGN KEY (`FK_adresse`) REFERENCES `adresse` (`id_adresse`),
  ADD CONSTRAINT `FKpersonne_adresse` FOREIGN KEY (`FK_personne`) REFERENCES `personne` (`id_personne`);

--
-- Contraintes pour la table `pers_travailler_dep`
--
ALTER TABLE `pers_travailler_dep`
  ADD CONSTRAINT `FKpers_travailler_dep` FOREIGN KEY (`FK_departement`) REFERENCES `departement` (`id_departement`),
  ADD CONSTRAINT `FKpers_travailler_dep_pers` FOREIGN KEY (`FK_personne`) REFERENCES `personne` (`id_personne`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
