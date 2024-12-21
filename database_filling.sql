-- Insert sample data for the Departement table
INSERT INTO departement (id, intitule) VALUES
(1, 'Human Resources'),
(2, 'Development'),
(3, 'Sales');

-- Insert sample data for the Utilisateur table
INSERT INTO utilisateur (id, nom, prenom, email, tel, tel_urgence, lien_urgence, nss, adresse, date_naissance, departement_id, photo, mot_de_passe, matricule) VALUES
(1, 'Doe', 'John', 'john.doe@example.com', '1234567890', '0987654321', 'spouse', '1234567890123', '123 Elm St', '1985-05-15', 2, 'photo1.jpg', 'password123', 'EMP001'),
(2, 'Smith', 'Jane', 'jane.smith@example.com', '1234567891', '0987654322', 'parent', '1234567890124', '456 Oak St', '1990-07-20', 1, 'photo2.jpg', 'password123', 'EMP002'),
(3, 'Brown', 'Alice', 'alice.brown@example.com', '1234567892', '0987654323', 'friend', '1234567890125', '789 Pine St', '1988-03-10', 3, 'photo3.jpg', 'password123', 'EMP003');

-- Insert sample data for the RH table
INSERT INTO rh (id_utilisateur) VALUES
(2);

-- Insert sample data for the Admin table
INSERT INTO admin (id_utilisateur) VALUES
(3);

-- Insert sample data for the Employe table
INSERT INTO employe (id_utilisateur) VALUES
(1),
(2),
(3);

-- Insert sample data for the Taches table
INSERT INTO taches (id, intitule, description, priorite, deadline) VALUES
(1, 'Prepare monthly report', 'Compile and submit the monthly sales report', 'MOYENNE', '2024-01-15'),
(2, 'Server maintenance', 'Perform routine server maintenance', 'ELEVEE', '2024-01-10'),
(3, 'Team building event', 'Organize a team-building activity', 'FAIBLE', '2024-02-01');

-- Insert sample data for the TachesAssignees table
INSERT INTO taches_assignees (employe_id, tache_id, statut) VALUES
(1, 1, 'NON_TERMINEE'),
(2, 2, 'TERMINEE'),
(3, 3, 'NON_TERMINEE');

-- Insert sample data for the Seuils table
INSERT INTO seuils (id, seuil_retard, seuil_absence, date_debut, date_fin) VALUES
(1, '00:15:00', 3, '2024-01-01', '2024-12-31');

-- Insert sample data for the Pointages table
INSERT INTO pointages (id, employe_id, date, heure_entree, heure_sortie) VALUES
(1, 1, '2024-01-02', '09:15:00', '17:00:00'),
(2, 2, '2024-01-02', '09:00:00', '17:00:00'),
(3, 3, '2024-01-02', '09:30:00', '17:00:00');

-- Insert sample data for the Absences table
INSERT INTO absences (pointage_id, justificatif) VALUES
(1, 'Medical note');

-- Insert sample data for the Retards table
INSERT INTO retards (pointage_id, retard, justificatif) VALUES
(3, '00:30:00', 'Traffic jam');

-- Insert sample data for the Notifications table
INSERT INTO notifications (id, employe_id, rh_id, statut) VALUES
(1, 1, 2, 'NON_ENVOYEE'),
(2, 3, 2, 'ENVOYEE');

-- Insert sample data for the Rappels table
INSERT INTO rappels (notification_id, employe_id, tache_id) VALUES
(1, 1, 1),
(2, 3, 3);

-- Insert sample data for the AvertissementsAbsence table
INSERT INTO avertissements_absence (notification_id, absence_id) VALUES
(1, 1);

-- Insert sample data for the AvertissementsRetard table
INSERT INTO avertissements_retard (notification_id, retard_id) VALUES
(2, 3);

-- Insert sample data for the Conges table
INSERT INTO conges (id, employe_id, type, date_debut, date_fin, statut, motif) VALUES
(1, 1, 'PERSONNEL', '2024-01-20', '2024-01-25', 'APPROUVE', 'Family event'),
(2, 2, 'MALADIE', '2024-01-05', '2024-01-10', 'EN_ATTENTE', 'Sick leave'),
(3, 3, 'RTT', '2024-02-01', '2024-02-05', 'REFUSE', 'Not eligible');
