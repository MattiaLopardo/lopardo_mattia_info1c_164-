DROP DATABASE IF EXISTS Lopardo_Mattia_INFO1C_EasyVista_164_2021;

CREATE DATABASE IF NOT EXISTS Lopardo_Mattia_INFO1C_EasyVista_164_2021;

USE Lopardo_Mattia_INFO1C_EasyVista_164_2021;

-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mer 08 Juin 2022 à 12:28
-- Version du serveur :  5.7.11
-- Version de PHP :  5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `lopardo_mattia_info1c_easyvista_164_2021`
--

-- --------------------------------------------------------

--
-- Structure de la table `t_adresse`
--

CREATE TABLE `t_adresse` (
  `id_adresse` int(11) NOT NULL,
  `nom_adresse` varchar(50) DEFAULT NULL,
  `NPA_adresse` int(25) DEFAULT NULL,
  `ville_adresse` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_adresse`
--

INSERT INTO `t_adresse` (`id_adresse`, `nom_adresse`, `NPA_adresse`, `ville_adresse`) VALUES
(1, 'via altisio 36', 1688, 'Sommentier'),
(2, 'Via Schliffras 98', 5637, 'Geltwil'),
(3, 'Via Franscini 6', 9327, 'Tübach'),
(4, 'Via Camischolas sura 4', 3036, 'Detligen'),
(5, 'Grossmatt 100', 8242, 'Bibern'),
(6, 'Via Gabbietta 29', 6653, 'Verscio'),
(7, 'Betburweg 128', 7058, 'Litzirüti'),
(8, 'Brunnacherstrasse 71', 3303, 'Zuzwil'),
(9, 'Fortunastrasse 81', 3423, 'Ersigen'),
(10, 'Valéestrasse 100', 1413, 'Oppens');

-- --------------------------------------------------------

--
-- Structure de la table `t_categorie`
--

CREATE TABLE `t_categorie` (
  `id_categorie` int(11) NOT NULL,
  `nom_categorie` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_categorie`
--

INSERT INTO `t_categorie` (`id_categorie`, `nom_categorie`) VALUES
(1, 'Bénéficiaire'),
(2, 'Technicien');

-- --------------------------------------------------------

--
-- Structure de la table `t_demande`
--

CREATE TABLE `t_demande` (
  `id_demande` int(11) NOT NULL,
  `nom_demande` varchar(40) DEFAULT NULL,
  `numero_demande` int(11) DEFAULT NULL,
  `description_demande` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_demande`
--

INSERT INTO `t_demande` (`id_demande`, `nom_demande`, `numero_demande`, `description_demande`) VALUES
(1, 'nouvel écran', 9983525, 'Le bénéficiare aimerait un nouveau écran pour travailler correctement'),
(2, 'nouvelle docking', 9924323, 'Le bénéficiare aimerait une nouvelle docking pour travailler correctement'),
(3, 'nouvelle souris', 9892444, 'Le bénéficiare aimerait une nouvelle souris pour travailler correctement'),
(4, 'nouveau clavier', 9821467, 'Le bénéficiare aimerait un nouveau clavier pour travailler correctement'),
(5, 'nouveau écran', 9977668, 'Le bénéficiare aimerait un nouveau écran pour travailler correctement');

-- --------------------------------------------------------

--
-- Structure de la table `t_incident`
--

CREATE TABLE `t_incident` (
  `id_incident` int(11) NOT NULL,
  `nom_incident` varchar(40) DEFAULT NULL,
  `numero_incident` int(11) DEFAULT NULL,
  `description_incident` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_incident`
--

INSERT INTO `t_incident` (`id_incident`, `nom_incident`, `numero_incident`, `description_incident`) VALUES
(1, 'laptop cassé', 9738754, 'Le bénéficiaire à besoin d\'un nouveau laptop au plus vite'),
(2, 'écran fissuré', 9718634, 'Le bénéficiaire à besoin d\'un nouveau écran au plus vite');

-- --------------------------------------------------------

--
-- Structure de la table `t_mail`
--

CREATE TABLE `t_mail` (
  `id_mail` int(11) NOT NULL,
  `nom_mail` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_mail`
--

INSERT INTO `t_mail` (`id_mail`, `nom_mail`) VALUES
(1, 'DupondPierre@eduvaud.vd'),
(2, 'WatsonMarie@eduvaud.vd'),
(3, 'pattinsonpeter@eduvaud.vd'),
(4, 'colehayden@eduvaud.vd'),
(5, 'briantjefferson@eduvaud.vd'),
(6, 'kobeanderson@eduvaud.vd'),
(7, 'JamesKarl@eduvaud.vd'),
(8, 'MoralesMiles@eduvaud.vd'),
(9, 'Pettersonkild@eduvaud.vd'),
(10, 'DwaneyDavide@eduvaud.vd');

-- --------------------------------------------------------

--
-- Structure de la table `t_personne`
--

CREATE TABLE `t_personne` (
  `id_personne` int(11) NOT NULL,
  `FK_mail` int(11) DEFAULT NULL,
  `FK_adresse` int(11) DEFAULT NULL,
  `FK_telephone` int(11) DEFAULT NULL,
  `nom_personne` varchar(30) DEFAULT NULL,
  `prenom_personne` varchar(30) DEFAULT NULL,
  `date_naiss_personne` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_personne`
--

INSERT INTO `t_personne` (`id_personne`, `FK_mail`, `FK_adresse`, `FK_telephone`, `nom_personne`, `prenom_personne`, `date_naiss_personne`) VALUES
(1, 1, 1, 1, 'Dupond', 'Pierre', '1994-08-10'),
(2, 2, 2, 2, 'Watson', 'Marie', '1993-10-12'),
(3, 3, 3, 3, 'pattinson', 'peter', '1980-01-09'),
(4, 4, 4, 4, 'cole', 'hayden', '1995-02-22'),
(5, 5, 5, 5, 'briant', 'jefferson', '2000-11-15'),
(6, 6, 6, 6, 'kobe', 'anderson', '2003-12-11'),
(7, 7, 7, 7, 'James', 'Karl', '2001-03-29'),
(8, 8, 8, 8, 'Morales', 'Miles', '2001-06-20'),
(9, 9, 9, 9, 'Petterson', 'kild', '2002-07-23'),
(10, 10, 10, 10, 'Dwaney', 'Davide', '1985-04-27');

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_attribuer_dem`
--

CREATE TABLE `t_pers_attribuer_dem` (
  `id_pers_attribuer_dem` int(11) NOT NULL,
  `FK_personne` int(11) DEFAULT NULL,
  `FK_demande` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_attribuer_dem`
--

INSERT INTO `t_pers_attribuer_dem` (`id_pers_attribuer_dem`, `FK_personne`, `FK_demande`) VALUES
(1, 5, 1),
(2, 6, 2),
(3, 7, 3),
(4, 8, 4),
(5, 9, 5);

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_attribuer_inc`
--

CREATE TABLE `t_pers_attribuer_inc` (
  `id_pers_attribuer_inc` int(11) NOT NULL,
  `FK_personne` int(11) DEFAULT NULL,
  `Fk_incident` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_attribuer_inc`
--

INSERT INTO `t_pers_attribuer_inc` (`id_pers_attribuer_inc`, `FK_personne`, `Fk_incident`) VALUES
(1, 10, 1),
(2, 6, 2);

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_auteur_dem`
--

CREATE TABLE `t_pers_auteur_dem` (
  `id_pers_auteur_dem` int(11) NOT NULL,
  `FK_personne` int(11) DEFAULT NULL,
  `FK_demande` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_auteur_dem`
--

INSERT INTO `t_pers_auteur_dem` (`id_pers_auteur_dem`, `FK_personne`, `FK_demande`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 1, 3),
(4, 2, 4),
(5, 1, 5);

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_auteur_inc`
--

CREATE TABLE `t_pers_auteur_inc` (
  `id_pers_auteur_inc` int(11) NOT NULL,
  `FK_personne` int(11) DEFAULT NULL,
  `FK_incident` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_auteur_inc`
--

INSERT INTO `t_pers_auteur_inc` (`id_pers_auteur_inc`, `FK_personne`, `FK_incident`) VALUES
(1, 3, 1),
(2, 4, 2);

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_categorie`
--

CREATE TABLE `t_pers_categorie` (
  `id_pers_categorie` int(11) NOT NULL,
  `FK_personne` int(11) NOT NULL,
  `FK_categorie` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_categorie`
--

INSERT INTO `t_pers_categorie` (`id_pers_categorie`, `FK_personne`, `FK_categorie`) VALUES
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 2),
(6, 6, 2),
(7, 7, 2),
(8, 8, 2),
(9, 9, 2),
(10, 10, 2),
(11, 1, 2);

-- --------------------------------------------------------

--
-- Structure de la table `t_telephone`
--

CREATE TABLE `t_telephone` (
  `id_telephone` int(11) NOT NULL,
  `num_telephone` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_telephone`
--

INSERT INTO `t_telephone` (`id_telephone`, `num_telephone`) VALUES
(1, 796544323),
(2, 795436787),
(3, 793458745),
(4, 796557623),
(5, 798775643),
(6, 794365489),
(7, 796346576),
(8, 798765684),
(9, 792769823),
(10, 798348629);

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_adresse`
--
ALTER TABLE `t_adresse`
  ADD PRIMARY KEY (`id_adresse`);

--
-- Index pour la table `t_categorie`
--
ALTER TABLE `t_categorie`
  ADD PRIMARY KEY (`id_categorie`);

--
-- Index pour la table `t_demande`
--
ALTER TABLE `t_demande`
  ADD PRIMARY KEY (`id_demande`);

--
-- Index pour la table `t_incident`
--
ALTER TABLE `t_incident`
  ADD PRIMARY KEY (`id_incident`);

--
-- Index pour la table `t_mail`
--
ALTER TABLE `t_mail`
  ADD PRIMARY KEY (`id_mail`);

--
-- Index pour la table `t_personne`
--
ALTER TABLE `t_personne`
  ADD PRIMARY KEY (`id_personne`),
  ADD KEY `FK_mail` (`FK_mail`),
  ADD KEY `FK_adresse` (`FK_adresse`),
  ADD KEY `FK_telephone` (`FK_telephone`);

--
-- Index pour la table `t_pers_attribuer_dem`
--
ALTER TABLE `t_pers_attribuer_dem`
  ADD PRIMARY KEY (`id_pers_attribuer_dem`),
  ADD KEY `FKpersonne_attr_dem` (`FK_personne`),
  ADD KEY `FKdem_attr` (`FK_demande`);

--
-- Index pour la table `t_pers_attribuer_inc`
--
ALTER TABLE `t_pers_attribuer_inc`
  ADD PRIMARY KEY (`id_pers_attribuer_inc`),
  ADD KEY `FKinc_attr_inc` (`Fk_incident`),
  ADD KEY `FKinc_attr_pers` (`FK_personne`);

--
-- Index pour la table `t_pers_auteur_dem`
--
ALTER TABLE `t_pers_auteur_dem`
  ADD PRIMARY KEY (`id_pers_auteur_dem`),
  ADD KEY `FKdem_auteur` (`FK_demande`),
  ADD KEY `FKdem_auteur_pers` (`FK_personne`);

--
-- Index pour la table `t_pers_auteur_inc`
--
ALTER TABLE `t_pers_auteur_inc`
  ADD PRIMARY KEY (`id_pers_auteur_inc`),
  ADD KEY `FKinc_auteur_pers` (`FK_personne`),
  ADD KEY `FKinc_auteur_inc` (`FK_incident`);

--
-- Index pour la table `t_pers_categorie`
--
ALTER TABLE `t_pers_categorie`
  ADD PRIMARY KEY (`id_pers_categorie`),
  ADD KEY `FKpersonne` (`FK_personne`),
  ADD KEY `FKcategorie` (`FK_categorie`);

--
-- Index pour la table `t_telephone`
--
ALTER TABLE `t_telephone`
  ADD PRIMARY KEY (`id_telephone`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_adresse`
--
ALTER TABLE `t_adresse`
  MODIFY `id_adresse` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT pour la table `t_categorie`
--
ALTER TABLE `t_categorie`
  MODIFY `id_categorie` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_demande`
--
ALTER TABLE `t_demande`
  MODIFY `id_demande` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT pour la table `t_incident`
--
ALTER TABLE `t_incident`
  MODIFY `id_incident` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `t_mail`
--
ALTER TABLE `t_mail`
  MODIFY `id_mail` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT pour la table `t_personne`
--
ALTER TABLE `t_personne`
  MODIFY `id_personne` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT pour la table `t_pers_attribuer_dem`
--
ALTER TABLE `t_pers_attribuer_dem`
  MODIFY `id_pers_attribuer_dem` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT pour la table `t_pers_attribuer_inc`
--
ALTER TABLE `t_pers_attribuer_inc`
  MODIFY `id_pers_attribuer_inc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `t_pers_auteur_dem`
--
ALTER TABLE `t_pers_auteur_dem`
  MODIFY `id_pers_auteur_dem` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT pour la table `t_pers_auteur_inc`
--
ALTER TABLE `t_pers_auteur_inc`
  MODIFY `id_pers_auteur_inc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `t_pers_categorie`
--
ALTER TABLE `t_pers_categorie`
  MODIFY `id_pers_categorie` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT pour la table `t_telephone`
--
ALTER TABLE `t_telephone`
  MODIFY `id_telephone` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `t_personne`
--
ALTER TABLE `t_personne`
  ADD CONSTRAINT `FK_adresse` FOREIGN KEY (`FK_adresse`) REFERENCES `t_adresse` (`id_adresse`),
  ADD CONSTRAINT `FK_mail` FOREIGN KEY (`FK_mail`) REFERENCES `t_mail` (`id_mail`),
  ADD CONSTRAINT `FK_telephone` FOREIGN KEY (`FK_telephone`) REFERENCES `t_telephone` (`id_telephone`);

--
-- Contraintes pour la table `t_pers_attribuer_dem`
--
ALTER TABLE `t_pers_attribuer_dem`
  ADD CONSTRAINT `FKdem_attr` FOREIGN KEY (`FK_demande`) REFERENCES `t_demande` (`id_demande`),
  ADD CONSTRAINT `FKpersonne_attr_dem` FOREIGN KEY (`FK_personne`) REFERENCES `t_personne` (`id_personne`);

--
-- Contraintes pour la table `t_pers_attribuer_inc`
--
ALTER TABLE `t_pers_attribuer_inc`
  ADD CONSTRAINT `FKinc_attr_inc` FOREIGN KEY (`Fk_incident`) REFERENCES `t_incident` (`id_incident`),
  ADD CONSTRAINT `FKinc_attr_pers` FOREIGN KEY (`FK_personne`) REFERENCES `t_personne` (`id_personne`);

--
-- Contraintes pour la table `t_pers_auteur_dem`
--
ALTER TABLE `t_pers_auteur_dem`
  ADD CONSTRAINT `FKdem_auteur` FOREIGN KEY (`FK_demande`) REFERENCES `t_demande` (`id_demande`),
  ADD CONSTRAINT `FKdem_auteur_pers` FOREIGN KEY (`FK_personne`) REFERENCES `t_personne` (`id_personne`);

--
-- Contraintes pour la table `t_pers_auteur_inc`
--
ALTER TABLE `t_pers_auteur_inc`
  ADD CONSTRAINT `FKinc_auteur_inc` FOREIGN KEY (`FK_incident`) REFERENCES `t_incident` (`id_incident`),
  ADD CONSTRAINT `FKinc_auteur_pers` FOREIGN KEY (`FK_personne`) REFERENCES `t_personne` (`id_personne`);

--
-- Contraintes pour la table `t_pers_categorie`
--
ALTER TABLE `t_pers_categorie`
  ADD CONSTRAINT `FK_categorie` FOREIGN KEY (`FK_categorie`) REFERENCES `t_categorie` (`id_categorie`),
  ADD CONSTRAINT `FK_personne` FOREIGN KEY (`FK_personne`) REFERENCES `t_personne` (`id_personne`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
