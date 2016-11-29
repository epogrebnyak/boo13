# -*- coding: utf-8 -*-
"""
"""

from subset import Subset

# bank projects
Subset(2015, 'temp').to_csv(force=True)


# Exclusions 1 (values do not change between 2015 and 2013):
ex1 = ['7733574312', '7703200101', '7726725828', '7116503278', '7720531939', '7802084784', '5261047820', '7717716979', '7707635583', '7707635618', '7707631814', '7707631780', '7707631807', '7707631797', '7707669230', '7707627840', '7710662717', '7707622136', '7707620724', '7707627776', '7710658157', '5906001179']
# Exclusions 2 (values not present in 2013, unit eq 385):
ex2 = ['6950089368', '7611020211', '7610052884', '8905049712', '2815015806', '6213008693', '1121012228', '1118005125', '1323126443', '7325134560', '6518008962', '7206025330', '2130035819', '7718000240', '5709000962', '2304030498', '1648030286', '3702549950', '2815014640', '2315097141', '3905069565', '2815006255', '6901077218', '4027094050', '6950086060', '7716239258', '7303018465', '7206045664', '1637001364', '7702845690', '7725261651', '6164029105', '6168079234', '6168084403', '7717795579', '7717536373', '7715801523', '4205301359', '4813012497', '5014010858', '4501092289', '4253006177', '5001101970', '5047117229', '3327846679', '2466134701', '2463256170', '7722347452', '7721160109', '7717045174', '7719592060', '6452117213', '6732039141', '5014011210', '1841013578', '2805005661', '6027165441', '2805003992', '7701681463', '3123322170', '2130152872', '6732110676', '7733561183', '7705506286', '7328077286', '5836140137', '6674188744', '6658444790', '2815000253', '7723683376', '3905049865', '2505006167', '6731079744', '1101029209', '3849003247', '7734549284', '4401126706', '7325037091', '7729781193', '6450942683', '7743929349', '7841345694', '5446014200', '2309112930', '7810414570', '6453123474', '7724892421', '3702037215', '7804011894', '5906088532', '4028057910', '7736049488', '7805304212', '3827041432', '2815005879', '1106020457', '1435120070', '6615000704', '7718622498', '2815015193', '7203315506', '2466202366', '2368006719', '7728260046', '7721692512', '4401145321', '7731293958', '7713791982', '6679065810', '4501165314', '3661054152', '6729041327', '3702654754', '5609174620', '2463223230', '7708231417', '7309901211', '3525335891', '7723624437', '2315983686', '6732004163', '3827034234', '3904070663', '7327058629', '5079011747', '5406755700', '4725001320', '7725253964', '6729019593', '3815015340', '5260398223', '2315096155', '5027112060', '6673243664', '5037009337', '3905069572', '7802803904', '9102015605', '7707785130', '7810593094', '6729018590', '3906262040', '5054009672', '6450046006', '7327026602', '6123023584', '7802510023', '7810804186', '7701996223', '6321360609', '6729019995', '5037003085', '7802877416', '7204009117', '5027229990', '5754003450', '7728011057', '7804528900', '7720292769', '7810345292', '5403196147', '7017273506', '7839477358', '6685035122', '7728509565', '6727051030', '7720719497', '6679060184', '2456007655', '7723361964', '7725563170', '7718107899', '3906206800', '7328001262', '3917017346', '6234143069', '7842511986', '7328073500', '6732031985', '6658460960', '2225145841', '7701414450', '7816477545', '7715230774', '7811451582', '7714774806', '6732067935', '7718590736', '6375190390', '7805286556', '1323124196', '2320222239', '5017099124', '7714002609', '7733259470', '7726263605', '7718036775', '6903006974', '1903022374', '2310127748', '6316151342', '1660028580', '7537011867', '6674336128', '7810895507', '7430008090', '9102173947', '7715030800', '7736527247', '5012052098', '7802178023', '7727224052', '3816006147', '7727180599', '7536102568', '1903005308', '7841323147', '7729747675', '6732073897', '7708256796', '2713015927', '3816006073', '5260380868', '7709736890', '7717535683', '5029160870', '6684004410', '7725844484', '7714775863', '7726080841', '7732115027', '7709864878', '7715556695', '7715789185', '3665073332', '7708091985', '4217103094', '6679054462', '7701385351', '5040087261', '5018151391', '4501107908', '7743689129', '7710062967', '7813229022', '7719065391', '7627024620', '6672181694', '7733005250', '7721762030', '4703044256', '6658425758', '6678006314', '7804069580', '6623071096', '6678003095', '6672339162', '1645030136', '7715441398', '5047121112', '7724589129', '6316133544', '2330029989', '7729642249']

#Subset(2015, 'base').exclude(ex1+ex2).to_csv(force=True)
