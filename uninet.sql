-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 21, 2026 at 02:51 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uninet`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumno`
--

CREATE TABLE `alumno` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `dni` int(15) NOT NULL,
  `telefono` varchar(30) NOT NULL,
  `promedio` float NOT NULL,
  `id_ciudad` int(11) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  `situacion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alumno`
--

INSERT INTO `alumno` (`id`, `nombre`, `apellido`, `email`, `pass`, `dni`, `telefono`, `promedio`, `id_ciudad`, `id_carrera`, `situacion`) VALUES
(1, 'joaquin', 'gonzalez', 'joaquingonzalez1@uca.edu.ar', '123joaquin', 545544545, '3242433553', 9.8, 1, 4, 'tipazo y fachero');

-- --------------------------------------------------------

--
-- Table structure for table `carrera`
--

CREATE TABLE `carrera` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `carrera`
--

INSERT INTO `carrera` (`id`, `nombre`) VALUES
(1, 'Ing. en Informatica'),
(2, 'Ingeniería en Sistemas'),
(3, 'Medicina'),
(4, 'Derecho'),
(5, 'Administración de Empresas'),
(6, 'Arquitectura'),
(7, 'Psicología'),
(8, 'Ingeniería Civil'),
(9, 'Contador Público'),
(10, 'Marketing'),
(11, 'Diseño Gráfico');

-- --------------------------------------------------------

--
-- Table structure for table `ciudad`
--

CREATE TABLE `ciudad` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ciudad`
--

INSERT INTO `ciudad` (`id`, `nombre`) VALUES
(1, 'Buenos Aires'),
(2, 'Córdoba'),
(3, 'Rosario'),
(4, 'Madrid'),
(5, 'Barcelona'),
(6, 'Ciudad de México'),
(7, 'Bogotá'),
(8, 'Santiago de Chile'),
(9, 'Lima'),
(10, 'Montevideo');

-- --------------------------------------------------------

--
-- Table structure for table `like`
--

CREATE TABLE `like` (
  `id` int(11) NOT NULL,
  `id_alumno` int(11) NOT NULL,
  `id_programa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `programa`
--

CREATE TABLE `programa` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `id_universidad` int(11) NOT NULL,
  `precio` double NOT NULL,
  `requisitos` text NOT NULL,
  `documento` varchar(100) NOT NULL,
  `modalidad` enum('hibrida','presencial','virtual') NOT NULL,
  `estado` enum('disponible','no disponible') NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `programa`
--

INSERT INTO `programa` (`id`, `nombre`, `id_universidad`, `precio`, `requisitos`, `documento`, `modalidad`, `estado`, `descripcion`) VALUES
(1, 'intercambio de redes', 1, 3456, 'promedio 8', '', 'virtual', 'disponible', 'aprender sobre redes de comunicacion'),
(2, 'curso de programacion poo', 1, 3454, '6.8 ingles fluido', '', 'presencial', 'disponible', 'aprendes sobre clases uml y java'),
(3, 'medicina aplicada', 1, 520, 'ingles avanzado, promedio 7.00', '', 'presencial', 'disponible', 'Formamos médicos con excelencia académica, sólida base científica y compromiso ético, preparados para diagnosticar, tratar y prevenir enfermedades con calidad humana y profesional.'),
(4, 'programacion web', 1, 0, '3er año de ing. informatica completado, conocimientos sobre js, html, css y python', '', 'virtual', 'disponible', 'Formamos desarrolladores capaces de diseñar, construir y mantener aplicaciones web modernas, combinando bases sólidas de programación con las últimas tecnologías del mercado.'),
(6, 'Italiano basico', 1, 0, '1er año completado en cualquier carrera', '', 'virtual', 'disponible', 'Aprendé los fundamentos del idioma italiano —gramática, vocabulario y pronunciación— para comunicarte con confianza en situaciones cotidianas.');

-- --------------------------------------------------------

--
-- Table structure for table `solicitud`
--

CREATE TABLE `solicitud` (
  `id` int(11) NOT NULL,
  `id_alumno` int(11) NOT NULL,
  `id_programa` int(11) NOT NULL,
  `fechahora` datetime NOT NULL,
  `estado` enum('solicitado','aceptado','rechazado') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `solicitud`
--

INSERT INTO `solicitud` (`id`, `id_alumno`, `id_programa`, `fechahora`, `estado`) VALUES
(1, 1, 1, '2026-05-08 19:41:33', 'aceptado'),
(2, 1, 2, '2026-05-08 20:26:24', 'aceptado'),
(3, 1, 4, '2026-07-18 11:56:00', 'aceptado');

-- --------------------------------------------------------

--
-- Table structure for table `universidad`
--

CREATE TABLE `universidad` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `id_ciudad` int(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `telefono` varchar(30) NOT NULL,
  `link` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `universidad`
--

INSERT INTO `universidad` (`id`, `nombre`, `id_ciudad`, `email`, `pass`, `telefono`, `link`) VALUES
(1, 'Universidad Catolica Argentina', 3, 'correouca@uca.edu.ar', 'cuentauca123', '11456798765', 'https://autogestion.uca.edu.ar/acceso');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumno`
--
ALTER TABLE `alumno`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `FK_id_carrera` (`id_carrera`),
  ADD KEY `FK_id_ciudad` (`id_ciudad`);

--
-- Indexes for table `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ciudad`
--
ALTER TABLE `ciudad`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `like`
--
ALTER TABLE `like`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_L_id_alumno` (`id_alumno`),
  ADD KEY `FK_L_id_programa` (`id_programa`);

--
-- Indexes for table `programa`
--
ALTER TABLE `programa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_P_id_universidad` (`id_universidad`);

--
-- Indexes for table `solicitud`
--
ALTER TABLE `solicitud`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_S_id_alumno` (`id_alumno`),
  ADD KEY `FK_S_id_programa` (`id_programa`);

--
-- Indexes for table `universidad`
--
ALTER TABLE `universidad`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `FK_U_id_ciudad` (`id_ciudad`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumno`
--
ALTER TABLE `alumno`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `carrera`
--
ALTER TABLE `carrera`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `ciudad`
--
ALTER TABLE `ciudad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `like`
--
ALTER TABLE `like`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `programa`
--
ALTER TABLE `programa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `solicitud`
--
ALTER TABLE `solicitud`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `universidad`
--
ALTER TABLE `universidad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `alumno`
--
ALTER TABLE `alumno`
  ADD CONSTRAINT `FK_id_carrera` FOREIGN KEY (`id_carrera`) REFERENCES `carrera` (`id`),
  ADD CONSTRAINT `FK_id_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id`);

--
-- Constraints for table `like`
--
ALTER TABLE `like`
  ADD CONSTRAINT `FK_L_id_alumno` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`id`),
  ADD CONSTRAINT `FK_L_id_programa` FOREIGN KEY (`id_programa`) REFERENCES `programa` (`id`);

--
-- Constraints for table `programa`
--
ALTER TABLE `programa`
  ADD CONSTRAINT `FK_P_id_universidad` FOREIGN KEY (`id_universidad`) REFERENCES `universidad` (`id`);

--
-- Constraints for table `solicitud`
--
ALTER TABLE `solicitud`
  ADD CONSTRAINT `FK_S_id_alumno` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`id`),
  ADD CONSTRAINT `FK_S_id_programa` FOREIGN KEY (`id_programa`) REFERENCES `programa` (`id`);

--
-- Constraints for table `universidad`
--
ALTER TABLE `universidad`
  ADD CONSTRAINT `FK_U_id_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
