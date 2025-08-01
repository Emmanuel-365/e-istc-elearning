/*==============================================================*/
/* Nom de SGBD :  Sybase SQL Anywhere 11                        */
/* Date de cr�ation :  7/22/2025 3:20:17 PM                     */
/*==============================================================*/


if exists(select 1 from sys.sysforeignkey where role='FK_ACTIVITE_ASSOCIATI_COURS') then
    alter table Activite
       delete foreign key FK_ACTIVITE_ASSOCIATI_COURS
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_ACTIVITE_ASSOCIATI_SOUMISSI') then
    alter table Activite
       delete foreign key FK_ACTIVITE_ASSOCIATI_SOUMISSI
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_ADMINIST_GENERALIS_UTILISAT') then
    alter table Administrateur
       delete foreign key FK_ADMINIST_GENERALIS_UTILISAT
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_COURS_ASSOCIATI_ENSEIGNA') then
    alter table Cours
       delete foreign key FK_COURS_ASSOCIATI_ENSEIGNA
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_ENSEIGNA_GENERALIS_UTILISAT') then
    alter table Enseignant
       delete foreign key FK_ENSEIGNA_GENERALIS_UTILISAT
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_ETUDIANT_GENERALIS_UTILISAT') then
    alter table Etudiant
       delete foreign key FK_ETUDIANT_GENERALIS_UTILISAT
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_FORUM_ASSOCIATI_COURS') then
    alter table Forum
       delete foreign key FK_FORUM_ASSOCIATI_COURS
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_INSCRIPT_ASSOCIATI_COURS') then
    alter table Inscription
       delete foreign key FK_INSCRIPT_ASSOCIATI_COURS
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_INSCRIPT_ASSOCIATI_ETUDIANT') then
    alter table Inscription
       delete foreign key FK_INSCRIPT_ASSOCIATI_ETUDIANT
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_MESSAGE_ASSOCIATI_UTILISAT') then
    alter table "Message"
       delete foreign key FK_MESSAGE_ASSOCIATI_UTILISAT
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_MODULE_ASSOCIATI_COURS') then
    alter table Module
       delete foreign key FK_MODULE_ASSOCIATI_COURS
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_NOTIFICA_ASSOCIATI_UTILISAT') then
    alter table Notification
       delete foreign key FK_NOTIFICA_ASSOCIATI_UTILISAT
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_QUESTION_ASSOCIATI_QUIZ') then
    alter table Question
       delete foreign key FK_QUESTION_ASSOCIATI_QUIZ
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_QUIZ_GENERALIS_ACTIVITE') then
    alter table Quiz
       delete foreign key FK_QUIZ_GENERALIS_ACTIVITE
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_RAPPORT_ASSOCIATI_ADMINIST') then
    alter table Rapport
       delete foreign key FK_RAPPORT_ASSOCIATI_ADMINIST
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_RESSOURC_ASSOCIATI_COURS') then
    alter table Ressource
       delete foreign key FK_RESSOURC_ASSOCIATI_COURS
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_SEESIONV_ASSOCIATI_COURS') then
    alter table SeesionVirtuelle
       delete foreign key FK_SEESIONV_ASSOCIATI_COURS
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_SOUMISSI_ASSOCIATI_ETUDIANT') then
    alter table Soumission
       delete foreign key FK_SOUMISSI_ASSOCIATI_ETUDIANT
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_TENTATIV_ASSOCIATI_ETUDIANT') then
    alter table Tentative
       delete foreign key FK_TENTATIV_ASSOCIATI_ETUDIANT
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_TENTATIV_ASSOCIATI_QUIZ') then
    alter table Tentative
       delete foreign key FK_TENTATIV_ASSOCIATI_QUIZ
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_17_FK'
     and t.table_name='Activite'
) then
   drop index Activite.ASSOCIATION_17_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_9_FK'
     and t.table_name='Activite'
) then
   drop index Activite.ASSOCIATION_9_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ACTIVITE_PK'
     and t.table_name='Activite'
) then
   drop index Activite.ACTIVITE_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Activite'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Activite
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='GENERALISATION_2_FK'
     and t.table_name='Administrateur'
) then
   drop index Administrateur.GENERALISATION_2_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ADMINISTRATEUR_PK'
     and t.table_name='Administrateur'
) then
   drop index Administrateur.ADMINISTRATEUR_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Administrateur'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Administrateur
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_15_FK'
     and t.table_name='Cours'
) then
   drop index Cours.ASSOCIATION_15_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='COURS_PK'
     and t.table_name='Cours'
) then
   drop index Cours.COURS_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Cours'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Cours
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='GENERALISATION_1_FK'
     and t.table_name='Enseignant'
) then
   drop index Enseignant.GENERALISATION_1_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ENSEIGNANT_PK'
     and t.table_name='Enseignant'
) then
   drop index Enseignant.ENSEIGNANT_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Enseignant'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Enseignant
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='GENERALISATION_3_FK'
     and t.table_name='Etudiant'
) then
   drop index Etudiant.GENERALISATION_3_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ETUDIANT_PK'
     and t.table_name='Etudiant'
) then
   drop index Etudiant.ETUDIANT_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Etudiant'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Etudiant
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_18_FK'
     and t.table_name='Forum'
) then
   drop index Forum.ASSOCIATION_18_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='FORUM_PK'
     and t.table_name='Forum'
) then
   drop index Forum.FORUM_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Forum'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Forum
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_14_FK'
     and t.table_name='Inscription'
) then
   drop index Inscription.ASSOCIATION_14_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_4_FK'
     and t.table_name='Inscription'
) then
   drop index Inscription.ASSOCIATION_4_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='INSCRIPTION_PK'
     and t.table_name='Inscription'
) then
   drop index Inscription.INSCRIPTION_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Inscription'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Inscription
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_1_FK'
     and t.table_name='Message'
) then
   drop index "Message".ASSOCIATION_1_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='MESSAGE_PK'
     and t.table_name='Message'
) then
   drop index "Message".MESSAGE_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Message'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table "Message"
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_7_FK'
     and t.table_name='Module'
) then
   drop index Module.ASSOCIATION_7_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='MODULE_PK'
     and t.table_name='Module'
) then
   drop index Module.MODULE_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Module'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Module
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_2_FK'
     and t.table_name='Notification'
) then
   drop index Notification.ASSOCIATION_2_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='NOTIFICATION_PK'
     and t.table_name='Notification'
) then
   drop index Notification.NOTIFICATION_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Notification'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Notification
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_13_FK'
     and t.table_name='Question'
) then
   drop index Question.ASSOCIATION_13_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='QUESTION_PK'
     and t.table_name='Question'
) then
   drop index Question.QUESTION_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Question'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Question
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='GENERALISATION_4_FK'
     and t.table_name='Quiz'
) then
   drop index Quiz.GENERALISATION_4_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='QUIZ_PK'
     and t.table_name='Quiz'
) then
   drop index Quiz.QUIZ_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Quiz'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Quiz
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_3_FK'
     and t.table_name='Rapport'
) then
   drop index Rapport.ASSOCIATION_3_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='RAPPORT_PK'
     and t.table_name='Rapport'
) then
   drop index Rapport.RAPPORT_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Rapport'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Rapport
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_8_FK'
     and t.table_name='Ressource'
) then
   drop index Ressource.ASSOCIATION_8_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='RESSOURCE_PK'
     and t.table_name='Ressource'
) then
   drop index Ressource.RESSOURCE_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Ressource'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Ressource
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_19_FK'
     and t.table_name='SeesionVirtuelle'
) then
   drop index SeesionVirtuelle.ASSOCIATION_19_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='SEESIONVIRTUELLE_PK'
     and t.table_name='SeesionVirtuelle'
) then
   drop index SeesionVirtuelle.SEESIONVIRTUELLE_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='SeesionVirtuelle'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table SeesionVirtuelle
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_10_FK'
     and t.table_name='Soumission'
) then
   drop index Soumission.ASSOCIATION_10_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='SOUMISSION_PK'
     and t.table_name='Soumission'
) then
   drop index Soumission.SOUMISSION_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Soumission'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Soumission
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_12_FK'
     and t.table_name='Tentative'
) then
   drop index Tentative.ASSOCIATION_12_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='ASSOCIATION_11_FK'
     and t.table_name='Tentative'
) then
   drop index Tentative.ASSOCIATION_11_FK
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='TENTATIVE_PK'
     and t.table_name='Tentative'
) then
   drop index Tentative.TENTATIVE_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Tentative'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Tentative
end if;

if exists(
   select 1 from sys.sysindex i, sys.systable t
   where i.table_id=t.table_id 
     and i.index_name='UTILISATEUR_PK'
     and t.table_name='Utilisateur'
) then
   drop index Utilisateur.UTILISATEUR_PK
end if;

if exists(
   select 1 from sys.systable 
   where table_name='Utilisateur'
     and table_type in ('BASE', 'GBL TEMP')
) then
    drop table Utilisateur
end if;

/*==============================================================*/
/* Table : Activite                                             */
/*==============================================================*/
create table Activite 
(
   idActivite           integer                        not null,
   Cou_idCours          integer                        not null,
   idSoumission         integer                        null,
   type                 varchar(254)                   null,
   titre                varchar(254)                   null,
   dateLimite           timestamp                      null,
   idCours              integer                        null,
   constraint PK_ACTIVITE primary key (idActivite)
);

/*==============================================================*/
/* Index : ACTIVITE_PK                                          */
/*==============================================================*/
create unique index ACTIVITE_PK on Activite (
idActivite ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_9_FK                                     */
/*==============================================================*/
create index ASSOCIATION_9_FK on Activite (
idSoumission ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_17_FK                                    */
/*==============================================================*/
create index ASSOCIATION_17_FK on Activite (
Cou_idCours ASC
);

/*==============================================================*/
/* Table : Administrateur                                       */
/*==============================================================*/
create table Administrateur 
(
   id                   integer                        not null,
   idAdmin              integer                        not null,
   constraint PK_ADMINISTRATEUR primary key (id, idAdmin)
);

/*==============================================================*/
/* Index : ADMINISTRATEUR_PK                                    */
/*==============================================================*/
create unique index ADMINISTRATEUR_PK on Administrateur (
id ASC,
idAdmin ASC
);

/*==============================================================*/
/* Index : GENERALISATION_2_FK                                  */
/*==============================================================*/
create index GENERALISATION_2_FK on Administrateur (
id ASC
);

/*==============================================================*/
/* Table : Cours                                                */
/*==============================================================*/
create table Cours 
(
   idCours              integer                        not null,
   id                   integer                        not null,
   idEnseignant         integer                        not null,
   titre                varchar(254)                   null,
   description          varchar(254)                   null,
   dateDebut            timestamp                      null,
   dateFin              timestamp                      null,
   statutCours          varchar(254)                   null,
   idEnseingnant        integer                        null,
   constraint PK_COURS primary key (idCours)
);

/*==============================================================*/
/* Index : COURS_PK                                             */
/*==============================================================*/
create unique index COURS_PK on Cours (
idCours ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_15_FK                                    */
/*==============================================================*/
create index ASSOCIATION_15_FK on Cours (
id ASC,
idEnseignant ASC
);

/*==============================================================*/
/* Table : Enseignant                                           */
/*==============================================================*/
create table Enseignant 
(
   id                   integer                        not null,
   idEnseignant         integer                        not null,
   specialite           integer                        null,
   statut               integer                        null,
   constraint PK_ENSEIGNANT primary key (id, idEnseignant)
);

/*==============================================================*/
/* Index : ENSEIGNANT_PK                                        */
/*==============================================================*/
create unique index ENSEIGNANT_PK on Enseignant (
id ASC,
idEnseignant ASC
);

/*==============================================================*/
/* Index : GENERALISATION_1_FK                                  */
/*==============================================================*/
create index GENERALISATION_1_FK on Enseignant (
id ASC
);

/*==============================================================*/
/* Table : Etudiant                                             */
/*==============================================================*/
create table Etudiant 
(
   id                   integer                        not null,
   Matricule            varchar(254)                   not null,
   niveau               varchar(254)                   null,
   formation            varchar(254)                   null,
   constraint PK_ETUDIANT primary key (id, Matricule)
);

/*==============================================================*/
/* Index : ETUDIANT_PK                                          */
/*==============================================================*/
create unique index ETUDIANT_PK on Etudiant (
id ASC,
Matricule ASC
);

/*==============================================================*/
/* Index : GENERALISATION_3_FK                                  */
/*==============================================================*/
create index GENERALISATION_3_FK on Etudiant (
id ASC
);

/*==============================================================*/
/* Table : Forum                                                */
/*==============================================================*/
create table Forum 
(
   idForum              integer                        not null,
   Cou_idCours          integer                        not null,
   sujet                varchar(254)                   null,
   idCours              integer                        null,
   constraint PK_FORUM primary key (idForum)
);

/*==============================================================*/
/* Index : FORUM_PK                                             */
/*==============================================================*/
create unique index FORUM_PK on Forum (
idForum ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_18_FK                                    */
/*==============================================================*/
create index ASSOCIATION_18_FK on Forum (
Cou_idCours ASC
);

/*==============================================================*/
/* Table : Inscription                                          */
/*==============================================================*/
create table Inscription 
(
   idInscription        integer                        not null,
   id                   integer                        not null,
   Matricule            varchar(254)                   not null,
   Cou_idCours          integer                        not null,
   dateInscription      timestamp                      null,
   statut               varchar(254)                   null,
   noteFinale           float                          null,
   idCours              integer                        null,
   MatriculeInsscription varchar(254)                   null,
   constraint PK_INSCRIPTION primary key (idInscription)
);

/*==============================================================*/
/* Index : INSCRIPTION_PK                                       */
/*==============================================================*/
create unique index INSCRIPTION_PK on Inscription (
idInscription ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_4_FK                                     */
/*==============================================================*/
create index ASSOCIATION_4_FK on Inscription (
id ASC,
Matricule ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_14_FK                                    */
/*==============================================================*/
create index ASSOCIATION_14_FK on Inscription (
Cou_idCours ASC
);

/*==============================================================*/
/* Table : "Message"                                            */
/*==============================================================*/
create table "Message" 
(
   idMessage            integer                        not null,
   id                   integer                        not null,
   contenu              varchar(254)                   null,
   dateEnvoi            timestamp                      null,
   expediteurid         integer                        null,
   destinataireid       integer                        null,
   constraint PK_MESSAGE primary key (idMessage)
);

/*==============================================================*/
/* Index : MESSAGE_PK                                           */
/*==============================================================*/
create unique index MESSAGE_PK on "Message" (
idMessage ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_1_FK                                     */
/*==============================================================*/
create index ASSOCIATION_1_FK on "Message" (
id ASC
);

/*==============================================================*/
/* Table : Module                                               */
/*==============================================================*/
create table Module 
(
   Cou_idCours          integer                        not null,
   idModule             integer                        not null,
   titre                varchar(254)                   null,
   ordre                integer                        null,
   idCours              integer                        null,
   constraint PK_MODULE primary key (Cou_idCours, idModule)
);

/*==============================================================*/
/* Index : MODULE_PK                                            */
/*==============================================================*/
create unique index MODULE_PK on Module (
Cou_idCours ASC,
idModule ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_7_FK                                     */
/*==============================================================*/
create index ASSOCIATION_7_FK on Module (
Cou_idCours ASC
);

/*==============================================================*/
/* Table : Notification                                         */
/*==============================================================*/
create table Notification 
(
   idNotification       integer                        not null,
   id                   integer                        not null,
   contenu              varchar(254)                   null,
   type                 varchar(254)                   null,
   idUser               integer                        null,
   constraint PK_NOTIFICATION primary key (idNotification)
);

/*==============================================================*/
/* Index : NOTIFICATION_PK                                      */
/*==============================================================*/
create unique index NOTIFICATION_PK on Notification (
idNotification ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_2_FK                                     */
/*==============================================================*/
create index ASSOCIATION_2_FK on Notification (
id ASC
);

/*==============================================================*/
/* Table : Question                                             */
/*==============================================================*/
create table Question 
(
   Act_idActivite       integer                        not null,
   Qui_idQuiz           integer                        not null,
   idQuestion           integer                        not null,
   intitule             varchar(254)                   null,
   typeQuestion         varchar(254)                   null,
   reponse_correcte     smallint                       null,
   idQuiz               integer                        null,
   constraint PK_QUESTION primary key (Act_idActivite, Qui_idQuiz, idQuestion)
);

/*==============================================================*/
/* Index : QUESTION_PK                                          */
/*==============================================================*/
create unique index QUESTION_PK on Question (
Act_idActivite ASC,
Qui_idQuiz ASC,
idQuestion ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_13_FK                                    */
/*==============================================================*/
create index ASSOCIATION_13_FK on Question (
Act_idActivite ASC,
Qui_idQuiz ASC
);

/*==============================================================*/
/* Table : Quiz                                                 */
/*==============================================================*/
create table Quiz 
(
   Act_idActivite       integer                        not null,
   idQuiz               integer                        not null,
   titreQuiz            varchar(254)                   null,
   duree                integer                        null,
   idActivite           integer                        null,
   constraint PK_QUIZ primary key (Act_idActivite, idQuiz)
);

/*==============================================================*/
/* Index : QUIZ_PK                                              */
/*==============================================================*/
create unique index QUIZ_PK on Quiz (
Act_idActivite ASC,
idQuiz ASC
);

/*==============================================================*/
/* Index : GENERALISATION_4_FK                                  */
/*==============================================================*/
create index GENERALISATION_4_FK on Quiz (
Act_idActivite ASC
);

/*==============================================================*/
/* Table : Rapport                                              */
/*==============================================================*/
create table Rapport 
(
   idRapport            integer                        not null,
   id                   integer                        not null,
   idAdmin              integer                        not null,
   type                 varchar(254)                   null,
   contenu              varchar(254)                   null,
   dateRapport          timestamp                      null,
   creer_par            varchar(254)                   null,
   constraint PK_RAPPORT primary key (idRapport)
);

/*==============================================================*/
/* Index : RAPPORT_PK                                           */
/*==============================================================*/
create unique index RAPPORT_PK on Rapport (
idRapport ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_3_FK                                     */
/*==============================================================*/
create index ASSOCIATION_3_FK on Rapport (
id ASC,
idAdmin ASC
);

/*==============================================================*/
/* Table : Ressource                                            */
/*==============================================================*/
create table Ressource 
(
   Cou_idCours          integer                        not null,
   idRessource          integer                        not null,
   nomFichier           varchar(254)                   null,
   Url                  varchar(254)                   null,
   format               varchar(254)                   null,
   idCours              integer                        null,
   constraint PK_RESSOURCE primary key (Cou_idCours, idRessource)
);

/*==============================================================*/
/* Index : RESSOURCE_PK                                         */
/*==============================================================*/
create unique index RESSOURCE_PK on Ressource (
Cou_idCours ASC,
idRessource ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_8_FK                                     */
/*==============================================================*/
create index ASSOCIATION_8_FK on Ressource (
Cou_idCours ASC
);

/*==============================================================*/
/* Table : SeesionVirtuelle                                     */
/*==============================================================*/
create table SeesionVirtuelle 
(
   idSession            integer                        not null,
   Cou_idCours          integer                        not null,
   lien                 varchar(254)                   null,
   dateSession          timestamp                      null,
   duree                integer                        null,
   idCours              integer                        null,
   constraint PK_SEESIONVIRTUELLE primary key (idSession)
);

/*==============================================================*/
/* Index : SEESIONVIRTUELLE_PK                                  */
/*==============================================================*/
create unique index SEESIONVIRTUELLE_PK on SeesionVirtuelle (
idSession ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_19_FK                                    */
/*==============================================================*/
create index ASSOCIATION_19_FK on SeesionVirtuelle (
Cou_idCours ASC
);

/*==============================================================*/
/* Table : Soumission                                           */
/*==============================================================*/
create table Soumission 
(
   idSoumission         integer                        not null,
   id                   integer                        not null,
   Matricule            varchar(254)                   not null,
   fichier              varchar(254)                   null,
   dateSoumission       timestamp                      null,
   note                 float                          null,
   idActivite           integer                        null,
   MatriculeSoumission  integer                        null,
   constraint PK_SOUMISSION primary key (idSoumission)
);

/*==============================================================*/
/* Index : SOUMISSION_PK                                        */
/*==============================================================*/
create unique index SOUMISSION_PK on Soumission (
idSoumission ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_10_FK                                    */
/*==============================================================*/
create index ASSOCIATION_10_FK on Soumission (
id ASC,
Matricule ASC
);

/*==============================================================*/
/* Table : Tentative                                            */
/*==============================================================*/
create table Tentative 
(
   idTentative          integer                        not null,
   id                   integer                        not null,
   Etu_Matricule        varchar(254)                   not null,
   Act_idActivite       integer                        not null,
   Qui_idQuiz           integer                        not null,
   dateTentative        timestamp                      null,
   dureeEffectuee       integer                        null,
   note                 float                          null,
   idQuiz               integer                        null,
   Matricule            varchar(254)                   null,
   constraint PK_TENTATIVE primary key (idTentative)
);

/*==============================================================*/
/* Index : TENTATIVE_PK                                         */
/*==============================================================*/
create unique index TENTATIVE_PK on Tentative (
idTentative ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_11_FK                                    */
/*==============================================================*/
create index ASSOCIATION_11_FK on Tentative (
id ASC,
Etu_Matricule ASC
);

/*==============================================================*/
/* Index : ASSOCIATION_12_FK                                    */
/*==============================================================*/
create index ASSOCIATION_12_FK on Tentative (
Act_idActivite ASC,
Qui_idQuiz ASC
);

/*==============================================================*/
/* Table : Utilisateur                                          */
/*==============================================================*/
create table Utilisateur 
(
   id                   integer                        not null,
   nom                  varchar(254)                   null,
   prenom               varchar(254)                   null,
   email                varchar(254)                   null,
   mot_de_passe         varchar(254)                   null,
   role                 varchar(254)                   null,
   constraint PK_UTILISATEUR primary key (id)
);

/*==============================================================*/
/* Index : UTILISATEUR_PK                                       */
/*==============================================================*/
create unique index UTILISATEUR_PK on Utilisateur (
id ASC
);

alter table Activite
   add constraint FK_ACTIVITE_ASSOCIATI_COURS foreign key (Cou_idCours)
      references Cours (idCours)
      on update restrict
      on delete restrict;

alter table Activite
   add constraint FK_ACTIVITE_ASSOCIATI_SOUMISSI foreign key (idSoumission)
      references Soumission (idSoumission)
      on update restrict
      on delete restrict;

alter table Administrateur
   add constraint FK_ADMINIST_GENERALIS_UTILISAT foreign key (id)
      references Utilisateur (id)
      on update restrict
      on delete restrict;

alter table Cours
   add constraint FK_COURS_ASSOCIATI_ENSEIGNA foreign key (id, idEnseignant)
      references Enseignant (id, idEnseignant)
      on update restrict
      on delete restrict;

alter table Enseignant
   add constraint FK_ENSEIGNA_GENERALIS_UTILISAT foreign key (id)
      references Utilisateur (id)
      on update restrict
      on delete restrict;

alter table Etudiant
   add constraint FK_ETUDIANT_GENERALIS_UTILISAT foreign key (id)
      references Utilisateur (id)
      on update restrict
      on delete restrict;

alter table Forum
   add constraint FK_FORUM_ASSOCIATI_COURS foreign key (Cou_idCours)
      references Cours (idCours)
      on update restrict
      on delete restrict;

alter table Inscription
   add constraint FK_INSCRIPT_ASSOCIATI_COURS foreign key (Cou_idCours)
      references Cours (idCours)
      on update restrict
      on delete restrict;

alter table Inscription
   add constraint FK_INSCRIPT_ASSOCIATI_ETUDIANT foreign key (id, Matricule)
      references Etudiant (id, Matricule)
      on update restrict
      on delete restrict;

alter table "Message"
   add constraint FK_MESSAGE_ASSOCIATI_UTILISAT foreign key (id)
      references Utilisateur (id)
      on update restrict
      on delete restrict;

alter table Module
   add constraint FK_MODULE_ASSOCIATI_COURS foreign key (Cou_idCours)
      references Cours (idCours)
      on update restrict
      on delete restrict;

alter table Notification
   add constraint FK_NOTIFICA_ASSOCIATI_UTILISAT foreign key (id)
      references Utilisateur (id)
      on update restrict
      on delete restrict;

alter table Question
   add constraint FK_QUESTION_ASSOCIATI_QUIZ foreign key (Act_idActivite, Qui_idQuiz)
      references Quiz (Act_idActivite, idQuiz)
      on update restrict
      on delete restrict;

alter table Quiz
   add constraint FK_QUIZ_GENERALIS_ACTIVITE foreign key (Act_idActivite)
      references Activite (idActivite)
      on update restrict
      on delete restrict;

alter table Rapport
   add constraint FK_RAPPORT_ASSOCIATI_ADMINIST foreign key (id, idAdmin)
      references Administrateur (id, idAdmin)
      on update restrict
      on delete restrict;

alter table Ressource
   add constraint FK_RESSOURC_ASSOCIATI_COURS foreign key (Cou_idCours)
      references Cours (idCours)
      on update restrict
      on delete restrict;

alter table SeesionVirtuelle
   add constraint FK_SEESIONV_ASSOCIATI_COURS foreign key (Cou_idCours)
      references Cours (idCours)
      on update restrict
      on delete restrict;

alter table Soumission
   add constraint FK_SOUMISSI_ASSOCIATI_ETUDIANT foreign key (id, Matricule)
      references Etudiant (id, Matricule)
      on update restrict
      on delete restrict;

alter table Tentative
   add constraint FK_TENTATIV_ASSOCIATI_ETUDIANT foreign key (id, Etu_Matricule)
      references Etudiant (id, Matricule)
      on update restrict
      on delete restrict;

alter table Tentative
   add constraint FK_TENTATIV_ASSOCIATI_QUIZ foreign key (Act_idActivite, Qui_idQuiz)
      references Quiz (Act_idActivite, idQuiz)
      on update restrict
      on delete restrict;

