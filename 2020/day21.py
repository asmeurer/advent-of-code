test_input = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

input = """
pnglkx nfnzx tjsdp jkbqk rpmqq gzgvdh rgdx szsbj xjdhk zfml ddbmq thvm mvnqdh gsgmdn dtlhh rqqfnlc bxv nthhxn hnmjfl ckqq qrsczjv fkh hkxcb rpcdfph flhfddq qspfqb zmb rpmmv zrgzf jfqqgtl xxfgvz kltcm xjrpr vnfmc xhmmt zkzdrn jmdg xgbvk ngqh hlmvqh djpsmd bnzq rbvdt tfmgl pjln (contains sesame, nuts)
qchnn dnpgcd zfml thvm gsgmdn frld nfnzx nqfc xbpb kltcm ljmvpp mrfxh zntrfp gzgvdh rrbndl pptgt rknm qsgb mstc ckqq zzldmh nggcjr bkd zfsks hlmvqh cxzkmr zmb tzjnvp npbnj lh pfqxsxd clqk rpmmv szsbj mnvq cnghsg jdtzr kfsfn jxjqp knqzf lvjpp qdpbx qrsczjv xxfgvz ngqh zrgzf jvvmcq zmcj dsmc xhmmt (contains sesame)
hlmvqh klmjmz clqk qrsczjv pjln lvjpp tbm thvm rqqfnlc gzgvdh klx sfk bnzq mhrm vht pjqdmpm tfmgl cxzkmr ghr rxrgtvs rfh rhrc vnfmc ljhn fbcds rkzhxmh htllnq zrgzf xhmmt rcr dgrrm xlzqfb xlnn ckqq vpgvm zntrfp jmdg pgqxp xjrpr vnmfg vqrjn thcs mnvq rczbvg bkd zqsc ngqh rpmqq zmcj cbbkfx rpcdfph mrfxh jfqqgtl mszc tzjnvp sdccxkt rcvd pcf xzcdnr jgtrnm zfcvnj dsmc gjqfj gtgrcf nthhxn jngghk hnmjfl qspfqb bxv (contains eggs)
nthhxn htllnq pbn qsgb mrfxh zrgzf dvcfx mstc jngghk xddkbd dpfphd zhghprj rfh ljmvpp vtljml pmtfmv zmb xxfgvz crnfzr xbpb jmdg tshn nqfc kmsh rknm hkqp pjqdmpm pjln ddbmq bjvcg zntrfp vnfmc qszmzsh fhtsl tjsdp kfsfn jkbqk thvm mnvq dnpgcd xzcdnr xjrpr rbvdt vht jxjqp zzldmh cnghsg pzxj jfqqgtl ckqq kqzcj lxr glrc dgrrm cxzkmr clqk xjdhk hlmvqh vpvj lbfgp klmjmz (contains dairy, peanuts, eggs)
rqqfnlc vgp tbm tjsdp tshn zzldmh zrgzf vgjbgj pptgt xnfhq pbn rpmmv dnpgcd qszmzsh rbvdt nzlks xddkbd thvm npbnj lxr szsbj dtlhh mrfxh ljmvpp xjzc zmb pjqdmpm rknm rrbndl xhmmt hlmvqh jmdg pjln pfqxsxd jdtzr jnr jkbqk vht vhcnpg ckqq ddgdhg pzxj ljhn xgbvk qfkjsq zhghprj gzgvdh xzcdnr ddbmq rcvd lbfgp mvnqdh rfh nggcjr gjqfj hrfmdk (contains dairy)
cmnb cnghsg cxzkmr vfkpj pgb xddkbd qfvfzg gzgvdh bxv zfml clqk pbn nthhxn jmdg ckqq rvchbn xbpb sfk dtlhh rqqfnlc rhrc djpsmd qrftr gjqfj bjvcg zntrfp qrsczjv thvm zlgztsbd lbfgp vnmfg jkbqk lvjpp pfqxsxd ljmvpp mrfxh mnvq ljhn fkh ddrd hlmvqh qmmt rcr vht xgbvk ddbmq tbm vhcnpg srgnx zrgzf ngqh mhrm pptgt glrc rpmmv kx htllnq (contains soy, shellfish)
fdf tshn zhghprj xjzc xxfgvz nggcjr hkqp vgjbgj ckqq hnmjfl mstc dmxhhd rpmmv jdtzr klx ngqh gtgrcf bjvcg vgp jgtrnm ttxx bcvmz pgqxp nfnzx sjgx zfcvnj tzjnvp qmmt jmdg qdpbx zmb rhrc gmc zfsks ljmvpp gjqfj fjgxv zttx lbskg vnfmc vfkpj lxr hkxcb dln xbpb sfk vpgvm thvm ljhn rknm rfh mgxzl thcs jfqqgtl bkd sdccxkt zzldmh mrfxh rcvd qchnn xhmmt rkzhxmh xgbvk csfmx zrgzf qrsczjv gzgvdh ncqdr rxr vtljml lbfgp pzxj djpsmd dpfphd rczbvg knnmm xmjlsn (contains nuts, dairy, sesame)
klx hkqp lqmfgp mstc mgxzl cxfzhj xxfgvz qrsczjv jxjqp ljhn pcf mrxg jmdg bjvcg vht lbskg tphtz nldzpc tjsdp mszc hlmvqh sfk dln ghr mppf lbfgp zkzdrn qdpbx bnzq qsgb rrbndl nggcjr zttx qjsbk llgsg srgnx dbx stcsp rcr zfml jvvmcq pptgt gmc fkh xjdhk pzxj zntrfp flhfddq knqzf ddrd jmgt fdf thcs lh mrfxh xmjlsn kglr pjqdmpm kx dpfphd vqrjn vhcnpg rxrgtvs pfqxsxd nqfc ckqq cbbkfx dtlhh thvm zmb qmmt xlzqfb rpmmv jfqqgtl gsgmdn bcvmz mnvq fbcds xjzc gtgrcf (contains nuts, sesame)
gzgvdh vbqbkt fjgxv nggcjr jvvmcq pptgt fmvvb zqsc hlmvqh rbvdt llgsg xddkbd rfh pjln tzjnvp glrc zmb rqqfnlc zttx qrsczjv rrbndl qfkjsq mppf rxrgtvs lvjpp dtlhh zfml stcsp zkzdrn vtljml qdpbx zrgzf fstgc xlnn sdccxkt hkxcb kltcm xlzqfb jfqqgtl npbnj bcvmz rknm ngqh xbpb rcr thvm kglr dbx xxfgvz bjvcg rpmmv srgnx ckqq gjqfj tshn gmc vgp dgrrm ljhn knnmm qkgqv mstc pnglkx flhfddq tjsdp jmdg zntrfp vgjbgj bkd (contains soy)
qjsbk fkh xddkbd fjgxv lbfgp rxr ckqq tphtz vhcnpg klmjmz pmtfmv jmdg hrfmdk dbx fbcds jnr xxfgvz pfqxsxd qfvfzg bxv flhfddq rknm rpmqq pjln sdccxkt pgb klx jdtzr zmb thvm hlmvqh lxr zrgzf nthhxn vnmfg jgtrnm nfnzx zzldmh ddbmq nldzpc tvqbhv dznd dnpgcd cmnb vpvj sjgx xjzc hkxcb szsbj dcbk pmvl pjqdmpm mhrm rgdx jfqqgtl zttx vtljml mrfxh cbbkfx knqzf mszc jkbqk xbpb vgjbgj pptgt vfkpj vqrjn zhghprj xnfhq tshn rcvd xjdhk djpsmd rfh glrc rkzhxmh (contains wheat, dairy)
mvnqdh nqfc bjvcg ckqq zfcvnj jmdg ljhn hkqp srgnx zfsks bxv xbpb rkzhxmh cxfzhj rpmqq zdntns dnpgcd thcs lvjpp klx jngghk flhfddq gmc pjln dcbk cbbkfx vbqbkt qchnn tshn fhtsl qmthj jvvmcq ncqdr jmgt csfmx qrsczjv tzjnvp rczbvg rcr hlmvqh rbvdt gtgrcf thvm cnghsg zrgzf rxrgtvs zmb (contains peanuts, soy)
ckqq frld mvnqdh tphtz bjvcg xzcdnr djpsmd ttxx dcbk qdpbx tshn rczbvg vpvj qmmt ddrd dln bxv zrgzf jxjqp lh mgxzl qrsczjv ltvr pbn nggcjr dsmc llgsg knnmm pzxj cnghsg thvm vnmfg mhrm xlnn gjqfj pptgt jkbqk htllnq jmdg xnfhq klx jmgt mrfxh rxr hnmjfl lqmfgp qrftr mppf sjgx rvchbn lvjpp mstc zqsc gmc kmsh rpmmv crnfzr hrfmdk kglr hlmvqh cxzkmr dvcfx (contains shellfish, eggs, dairy)
xjrpr mjpt cbbkfx rpmqq ljhn jmdg vht sdccxkt ngqh bnzq jgtrnm fmvvb mrfxh xxfgvz jfqqgtl tfmgl bcvmz pgqxp thvm crnfzr xddkbd zfsks qrsczjv pzxj tshn fbcds lbfgp thcs hkqp gsgmdn dvcfx zmb cnghsg csfmx vhqfz rxr bxv xjdhk zhghprj dtlhh ckqq qmthj jxjqp rczbvg gmc sfk ttxx ltvr pnglkx dnpgcd qsgb clqk klmjmz lh rvchbn pjln knqzf vnfmc qspfqb nthhxn zqsc mhrm gzgvdh ncqdr zrgzf ddrd vqrjn (contains nuts, shellfish)
rvchbn vhcnpg mstc zrgzf hkqp bnzq xbpb qrsczjv fhtsl fjgxv ddgdhg jfqqgtl rpmqq dpfphd pcf qrftr ngqh vht dvcfx dfrg tphtz mnvq qjsbk mvnqdh zntrfp xjzc jmgt xzcdnr vnfmc xddkbd fkh kmsh xmjlsn ckqq zfsks bcvmz ljhn gmc rrbndl fmvvb cxzkmr lh zdntns pgb thvm xxfgvz hrfmdk dln mrfxh tvqbhv cnghsg vpgvm hlmvqh mjpt jdtzr dgrrm kglr pgqxp kqzcj hkxcb xgbvk djpsmd tshn klmjmz rfh xlnn bjvcg qfkjsq rkzhxmh glrc clqk gjqfj jmdg knqzf ljmvpp csfmx rbvdt zfcvnj dsmc fstgc (contains dairy)
nthhxn vnfmc dsmc vpvj rhrc zfcvnj zdntns qmthj knnmm rpmmv dtlhh qdpbx zhghprj xddkbd mrfxh rqqfnlc dpfphd xhmmt dgrrm pgqxp zmb gmc flhfddq zkzdrn hlmvqh qrsczjv vhcnpg mjpt fbcds thvm ncqdr pjln zttx hrfmdk xlnn dvcfx fkh mszc klx cmnb zfml zrgzf mnvq rcr bjvcg csfmx xlzqfb ckqq (contains sesame, shellfish)
xnfhq hlmvqh lh qdpbx rpcdfph qsgb rpmqq tjsdp ljhn gsgmdn vfkpj jmdg xlzqfb ckqq qmmt jmgt dvcfx zrgzf bkd pmvl ngqh sjgx dpfphd kfsfn mrfxh bjvcg jkbqk qrftr mjpt vnmfg nldzpc ncqdr jvvmcq pptgt pjqdmpm thvm pjln ddrd csfmx kglr xgbvk tzjnvp bxv htllnq fstgc zfcvnj jxjqp pbn dsmc kbtx vqrjn rqqfnlc rxrgtvs hnmjfl qrsczjv (contains eggs)
mvnqdh klx rbvdt kx qmthj hrfmdk bcvmz fhtsl zrgzf xxfgvz pmvl csfmx hkxcb rpmqq vpvj jmgt vbqbkt lxr hlmvqh zhghprj kglr dpfphd xzcdnr mszc vgp dvcfx gzgvdh ncqdr mppf nldzpc djpsmd pnglkx mrfxh lqmfgp sjgx jfqqgtl dln vhcnpg npbnj cmnb hnmjfl kfsfn vtljml qspfqb xlzqfb dcbk jngghk lh jxjqp rxr jdtzr qrftr fbcds thvm mrxg zzldmh qfvfzg dtlhh hkqp dsmc qdpbx cxzkmr tfmgl xjrpr pjqdmpm rczbvg rcvd lbfgp jmdg qszmzsh glrc qkgqv tvqbhv qrsczjv fkh rknm ckqq zntrfp cbbkfx (contains shellfish, dairy)
zqsc zmb sfk thvm lvjpp ddgdhg qrsczjv qspfqb dmxhhd zzldmh xzcdnr xjdhk dznd qfvfzg ljhn ghr zrgzf bcvmz frld pnglkx fhtsl srgnx jfqqgtl fdf vhqfz qsgb jkbqk ckqq xxfgvz pjqdmpm rpmqq jmdg fkh crnfzr mjpt cnghsg qrftr xddkbd rkzhxmh pfqxsxd mhrm gtgrcf hlmvqh fmvvb tvqbhv dgrrm xbpb qmthj gjqfj kqzcj tshn qkgqv vfkpj kmsh pgqxp ddrd glrc xgbvk hrfmdk rgdx bnzq knnmm qchnn vnmfg ncqdr qfkjsq pmtfmv xnfhq sjgx cbbkfx stcsp rbvdt mstc gzgvdh kglr dsmc rrbndl xjzc rpcdfph (contains nuts)
rbvdt jmdg zkzdrn zmb hnmjfl gmc pgqxp lqmfgp knqzf xbpb fmvvb bkd dgrrm vgjbgj dcbk ttxx dtlhh vpgvm xlnn hlmvqh jgtrnm dpfphd qrsczjv xzcdnr jngghk qmmt thvm flhfddq gzgvdh crnfzr qszmzsh xlzqfb dfrg qspfqb qmthj rpcdfph frld zqsc xjdhk dmxhhd ljhn qchnn bnzq kltcm gtgrcf mszc zhghprj rhrc csfmx mrxg klmjmz lbskg ckqq pzxj nggcjr nthhxn nldzpc rpmqq dbx mhrm zrgzf xjzc (contains dairy, wheat, eggs)
lh sfk jvvmcq szsbj fmvvb xxfgvz sjgx jnr vqrjn gmc cnghsg qsgb jmdg mppf jfqqgtl fjgxv vbqbkt zqsc xgbvk pgqxp nqfc jmgt rfh xlnn rhrc nfnzx rpcdfph qszmzsh kglr zmb xnfhq thvm tbm zzldmh rcvd pmvl kqzcj hnmjfl nggcjr qrsczjv qchnn zmcj rvchbn fdf xmjlsn mnvq mgxzl rkzhxmh bxv ngqh xlzqfb gjqfj sdccxkt clqk cmnb rbvdt jkbqk dpfphd mrfxh hlmvqh kltcm ckqq jngghk mszc (contains sesame)
zfcvnj mvnqdh gjqfj htllnq nggcjr vtljml qrftr fstgc xjrpr dvcfx klmjmz thvm qjsbk rcvd hrfmdk rczbvg mjpt ncqdr kbtx nqfc xxfgvz xlzqfb mrfxh zmb jkbqk jmgt rxrgtvs qspfqb rhrc qmthj mszc ghr fmvvb cxfzhj lqmfgp ckqq zrgzf vfkpj tzjnvp mhrm vpvj pgqxp ngqh xlnn hlmvqh xnfhq tbm zqsc jvvmcq rvchbn lxr qrsczjv vgp cmnb pjqdmpm (contains dairy)
qfvfzg ngqh rhrc nthhxn mvnqdh rcr knnmm zmcj nfnzx stcsp nzlks qdpbx kfsfn nldzpc mrfxh cxzkmr fkh vpvj llgsg pgb cmnb ncqdr qchnn zrgzf rknm xjzc zntrfp mstc clqk gsgmdn jnr ljhn mppf hkqp jmdg xlnn xgbvk csfmx rpmmv fmvvb mjpt thvm zlgztsbd dtlhh dln bnzq klmjmz tfmgl vgp qmmt kglr dbx gzgvdh rcvd kmsh rgdx kqzcj ttxx tzjnvp qmthj hlmvqh zfsks qrsczjv lh vhcnpg pgqxp zmb zhghprj vht rxr vbqbkt pcf gtgrcf zzldmh dvcfx (contains wheat)
vfkpj kbtx qkgqv bkd srgnx rcr zdntns tjsdp kfsfn rhrc mstc vtljml zlgztsbd rbvdt zrgzf glrc qfvfzg rkzhxmh ddbmq pbn flhfddq dfrg kglr clqk rxrgtvs cxzkmr mrfxh ddgdhg cmnb hlmvqh rpmmv dln zttx pjln zmb pjqdmpm jmgt ckqq qdpbx rcvd thvm rrbndl vbqbkt xmjlsn lh xhmmt qmthj nzlks pgb xzcdnr mrxg xgbvk fkh vgp rqqfnlc gjqfj gsgmdn tbm szsbj bxv lxr cnghsg jfqqgtl dbx pmtfmv lvjpp xjzc xlnn dtlhh dsmc vnfmc qrsczjv zkzdrn ghr fhtsl (contains dairy, wheat, peanuts)
nldzpc pbn rxr vgp zmb pgqxp zfsks vfkpj tvqbhv qmmt pjln jmdg qfkjsq hnmjfl mrxg hlmvqh dln nqfc lbfgp rcr kfsfn vtljml rxrgtvs tbm dsmc hkqp lh jngghk vbqbkt thvm fbcds clqk pjqdmpm ckqq mppf tzjnvp xhmmt csfmx rpcdfph sdccxkt kbtx knqzf rkzhxmh qrsczjv mszc ttxx klx mrfxh mnvq (contains dairy, sesame)
rgdx tfmgl gmc fstgc ltvr ckqq pnglkx kglr hkqp ddgdhg qfkjsq xzcdnr jnr xxfgvz hlmvqh zhghprj ghr pfqxsxd ljmvpp zmb cmnb nldzpc dznd xlnn zrgzf lh zfcvnj dcbk kmsh xjrpr qjsbk nzlks gtgrcf kfsfn dpfphd rqqfnlc mppf zzldmh thcs cbbkfx jmgt rcr pjln mrfxh jxjqp fmvvb pmvl mgxzl knqzf rbvdt gzgvdh jmdg qrsczjv nqfc vnmfg qszmzsh tjsdp ljhn qrftr ddbmq bkd fbcds (contains wheat, peanuts)
clqk rpmmv rkzhxmh pbn mrfxh pmvl hkxcb mvnqdh kbtx tzjnvp ncqdr kmsh dcbk zrgzf qchnn bkd kqzcj hlmvqh thvm cmnb mjpt knnmm pzxj frld gsgmdn pfqxsxd ltvr lqmfgp fkh rbvdt vgjbgj nldzpc jgtrnm dbx qrftr zdntns lbskg rpcdfph djpsmd vbqbkt dsmc jdtzr qmthj zmb hnmjfl sfk mppf fmvvb rcr xmjlsn qrsczjv csfmx dln vqrjn xbpb stcsp fdf rxrgtvs mstc jmdg ljhn npbnj thcs ddbmq knqzf dgrrm rqqfnlc mszc jnr lbfgp qsgb dtlhh pgb bcvmz qszmzsh rfh gjqfj xlzqfb rxr (contains peanuts)
clqk csfmx lvjpp kqzcj thvm zntrfp dcbk ghr vtljml pfqxsxd pjqdmpm jgtrnm flhfddq zzldmh llgsg nthhxn mjpt zrgzf pjln dznd mnvq bjvcg nfnzx tzjnvp vgp dtlhh qmmt rpmmv jmdg zfcvnj xzcdnr zmb tbm dbx bxv cxzkmr tfmgl mszc ttxx qkgqv qjsbk ckqq pgqxp zfml mhrm vpvj jdtzr mgxzl tvqbhv qfvfzg vhcnpg lbskg lqmfgp cnghsg rcvd hnmjfl zhghprj hlmvqh xjrpr xxfgvz dln gtgrcf sdccxkt kx qspfqb jfqqgtl pptgt dmxhhd rpcdfph fstgc rcr fmvvb ljmvpp mrxg gmc pgb mrfxh kmsh cmnb (contains soy, wheat, eggs)
klx nggcjr xjrpr zdntns kltcm vhcnpg xlnn kqzcj hlmvqh dnpgcd vht rpmmv bnzq hnmjfl lbskg fdf bkd dgrrm rvchbn mgxzl pgb jdtzr dcbk qszmzsh rpmqq hrfmdk qrftr dpfphd lxr ngqh xddkbd qrsczjv tbm vqrjn qchnn vpvj mstc ckqq pbn zrgzf jxjqp jgtrnm tfmgl zmb rqqfnlc xmjlsn rxr pmtfmv zmcj zfsks zqsc crnfzr jmdg fbcds mrfxh xgbvk hkxcb gmc nldzpc nfnzx xnfhq (contains peanuts, eggs, nuts)
csfmx zzldmh dcbk fdf rhrc fjgxv qchnn cxzkmr qmthj crnfzr nqfc zmcj mhrm ltvr sdccxkt flhfddq cbbkfx cmnb qdpbx thvm xmjlsn fhtsl knqzf bxv nggcjr vnmfg zmb cxfzhj jdtzr pnglkx jmdg lxr kmsh vgjbgj mrfxh dln mppf gzgvdh rpmmv zntrfp zrgzf pgqxp ckqq zfml vnfmc vht pmvl xlzqfb rxrgtvs kltcm pzxj dsmc dtlhh hrfmdk qmmt dnpgcd bjvcg gsgmdn cnghsg xhmmt gmc ttxx qjsbk hlmvqh fkh vhqfz xxfgvz (contains dairy, sesame, eggs)
jmgt mppf ttxx dsmc xnfhq bxv kglr bcvmz ckqq jmdg dfrg jnr mnvq ngqh sfk fdf xhmmt fjgxv zfcvnj rczbvg cmnb xjrpr szsbj dvcfx gtgrcf knqzf pjln mrfxh lbfgp vnmfg jdtzr mhrm fstgc tbm djpsmd pnglkx qkgqv zmb vfkpj hkxcb qfkjsq pgqxp xzcdnr nfnzx npbnj rbvdt jfqqgtl hlmvqh qfvfzg jvvmcq hnmjfl thvm rgdx gjqfj zhghprj kqzcj rcr zrgzf tvqbhv tshn (contains peanuts)
rknm lvjpp cnghsg qrsczjv sdccxkt zrgzf rcvd rxrgtvs stcsp thvm fstgc ttxx pmvl rpcdfph dznd ckqq pptgt mstc rpmmv fdf knnmm jnr bjvcg mnvq qdpbx zfml rqqfnlc zqsc zhghprj mgxzl qmmt fkh rxr dsmc lbskg sfk xhmmt kqzcj vfkpj mhrm hlmvqh mrfxh pcf zmb jmgt ljmvpp jfqqgtl szsbj xjrpr vnfmc qszmzsh dbx mszc xlnn qrftr qchnn mjpt zttx ddgdhg gmc djpsmd zfcvnj dln qkgqv rcr dnpgcd tzjnvp hkxcb zmcj lxr bcvmz fhtsl vnmfg vpgvm (contains dairy, sesame)
rgdx jmdg cmnb thvm fstgc pfqxsxd ncqdr dmxhhd glrc xjrpr rkzhxmh fhtsl mrfxh hkxcb pmtfmv zfsks knnmm pgb vnmfg thcs dfrg ddbmq clqk zntrfp nthhxn xjzc dgrrm lvjpp rpmmv vht lh jfqqgtl vgp mszc rczbvg jnr jngghk xhmmt vhqfz bcvmz zmb ckqq tjsdp bkd xlzqfb xddkbd pmvl qrsczjv ddgdhg djpsmd ttxx zfcvnj mjpt nldzpc qrftr kx xnfhq fjgxv jmgt ljhn mrxg pbn sdccxkt rxrgtvs dln dpfphd zrgzf tbm rfh tvqbhv (contains sesame, dairy, shellfish)
rczbvg cxfzhj lxr mgxzl hkxcb kbtx zmb jvvmcq pmtfmv jfqqgtl jxjqp mszc thvm rknm jmdg vfkpj qmmt hlmvqh ltvr cnghsg pjln mrfxh gzgvdh szsbj pgb dcbk lvjpp qchnn bcvmz sdccxkt llgsg xgbvk mrxg ghr zhghprj hkqp thcs zrgzf zzldmh ckqq frld gtgrcf pnglkx clqk kglr xhmmt hnmjfl qjsbk qfvfzg dnpgcd dbx djpsmd qrftr rgdx tvqbhv ncqdr (contains eggs)
pmvl zmb zrgzf rxrgtvs mvnqdh dznd srgnx qmmt pgb jmdg hlmvqh dgrrm xjdhk klx rcvd qrsczjv cnghsg ttxx hrfmdk qspfqb pfqxsxd fmvvb pzxj sfk rbvdt nggcjr zqsc npbnj kglr xddkbd lbskg lqmfgp mrxg mrfxh zfml rkzhxmh jfqqgtl vgjbgj rpmmv tphtz mszc dln zfcvnj vpgvm tzjnvp rhrc nldzpc rknm tshn jgtrnm mppf fjgxv ckqq ddgdhg vpvj fbcds (contains shellfish)
xlzqfb nthhxn dln rczbvg jmdg vgp cbbkfx gsgmdn jvvmcq glrc klmjmz stcsp bcvmz dbx vpvj cmnb sjgx rfh rrbndl mgxzl jnr rhrc thvm xlnn mhrm mrfxh bxv qrftr lvjpp fjgxv kglr cxfzhj zmb pptgt ghr kbtx pnglkx qjsbk ckqq jfqqgtl fstgc dznd qszmzsh jgtrnm zrgzf tjsdp klx pjln vgjbgj vbqbkt zkzdrn sfk qrsczjv vhqfz hrfmdk kltcm vnfmc zqsc xhmmt knnmm qfvfzg xjrpr nqfc jkbqk (contains nuts, sesame)
jgtrnm bxv fbcds dznd bkd ttxx rpmqq ckqq pmvl dtlhh xjdhk zdntns knnmm vqrjn dsmc lqmfgp ltvr jfqqgtl mszc xhmmt szsbj crnfzr fkh rbvdt pjqdmpm nggcjr qrftr bcvmz qmmt srgnx xddkbd rvchbn zmb cmnb pptgt xjzc llgsg rxr bnzq gsgmdn thvm zzldmh rcvd mrfxh dgrrm zfsks qsgb tvqbhv zkzdrn nzlks lh klmjmz rxrgtvs kqzcj mnvq ngqh rczbvg tshn tjsdp hlmvqh pcf fdf rfh pnglkx hkqp zrgzf jkbqk sdccxkt fstgc vpvj ddbmq zttx xlzqfb qfvfzg frld qrsczjv zlgztsbd xnfhq pfqxsxd cxfzhj cxzkmr tphtz clqk (contains shellfish, peanuts)
hrfmdk nthhxn lh zrgzf thvm rbvdt qdpbx mhrm vhqfz lqmfgp qjsbk vgp qfvfzg szsbj nldzpc vpgvm sdccxkt dgrrm tfmgl zdntns ddgdhg zfsks hlmvqh zmcj pnglkx ncqdr qrsczjv sfk mrfxh rqqfnlc vht mstc pmvl cmnb gmc ckqq jmdg thcs bjvcg nzlks klx jfqqgtl fkh ghr ddbmq htllnq xlnn kglr (contains nuts)
fkh knqzf tvqbhv mrfxh hkqp nqfc mvnqdh xxfgvz gzgvdh vnfmc qrftr qrsczjv ngqh cxzkmr mjpt dvcfx zmcj xddkbd clqk rvchbn dsmc xjzc pfqxsxd dfrg qmmt mhrm flhfddq rrbndl xnfhq hlmvqh jmdg dznd frld jnr djpsmd thvm qjsbk ddbmq qchnn pnglkx dtlhh zhghprj fhtsl vtljml nzlks qszmzsh lqmfgp pbn cmnb rpcdfph kx qkgqv zrgzf tshn zmb zlgztsbd xlnn (contains eggs, nuts, dairy)
gsgmdn zqsc cxzkmr xlnn htllnq vbqbkt pgb pnglkx tphtz jmgt mrfxh qkgqv pjqdmpm glrc sdccxkt rbvdt vht pzxj fstgc bcvmz mjpt dvcfx vpvj ljmvpp pfqxsxd tshn zmcj zrgzf qmmt pcf dpfphd xxfgvz jxjqp rczbvg mgxzl thvm fjgxv hnmjfl rkzhxmh qrsczjv jmdg cnghsg zfml gjqfj tbm lh mppf dcbk zntrfp dbx jvvmcq szsbj pjln xhmmt rcr nthhxn kx fmvvb xzcdnr klx rpcdfph zmb djpsmd jdtzr mnvq hlmvqh bjvcg mrxg (contains eggs)
vqrjn rhrc pzxj pjqdmpm tshn pjln nggcjr ljhn fkh qchnn kfsfn vgjbgj jmgt qkgqv stcsp knnmm dznd pgb csfmx fmvvb ltvr rknm rpcdfph thvm mrfxh qfvfzg zfcvnj zmb clqk kx ghr rpmmv vbqbkt tfmgl dfrg lxr hrfmdk vpgvm zlgztsbd rczbvg tvqbhv jnr qjsbk qfkjsq xxfgvz hlmvqh klx dnpgcd kbtx flhfddq jfqqgtl jmdg ddrd xgbvk rqqfnlc ckqq bnzq mnvq ncqdr dln qdpbx kltcm mppf zttx dbx pmtfmv klmjmz vnmfg pgqxp nthhxn crnfzr dmxhhd xhmmt rgdx mvnqdh gsgmdn nzlks xzcdnr fbcds djpsmd zfsks dpfphd lh ddbmq vfkpj vgp qrsczjv (contains peanuts, eggs, soy)
dsmc hlmvqh rqqfnlc dgrrm lbskg xxfgvz klmjmz jmgt jnr dznd npbnj rrbndl fkh vfkpj dvcfx hnmjfl qrftr pmtfmv kltcm xzcdnr gtgrcf lbfgp bcvmz xddkbd vgjbgj gjqfj kglr qchnn zlgztsbd rcvd xmjlsn bnzq kbtx vnfmc zmb srgnx pptgt llgsg thvm ckqq qrsczjv cbbkfx cnghsg xjzc rbvdt mnvq mrfxh mppf rknm jmdg tzjnvp rfh vgp vpvj nfnzx hkxcb zqsc lqmfgp kmsh dnpgcd sjgx sfk gmc jfqqgtl ltvr vpgvm pmvl qmthj klx tbm rvchbn pfqxsxd xjdhk glrc rczbvg knqzf (contains shellfish, dairy, nuts)
ngqh lxr qrftr nldzpc cbbkfx zdntns xxfgvz srgnx qspfqb zfsks tzjnvp tphtz qrsczjv lbfgp gjqfj xjrpr qfkjsq rfh xgbvk dtlhh mrfxh xjdhk qkgqv hkqp dsmc rczbvg klmjmz ckqq xlzqfb ddgdhg kltcm vhqfz kglr jxjqp xddkbd htllnq gtgrcf zrgzf lbskg gmc szsbj thvm zmb zfcvnj hlmvqh pjqdmpm (contains peanuts, shellfish)
xlzqfb vpgvm flhfddq kbtx zmcj jmdg vhqfz tphtz vqrjn stcsp ckqq rgdx nfnzx nggcjr qrsczjv xmjlsn pgb ngqh pjqdmpm qsgb nldzpc hkxcb klmjmz rpmmv xjrpr zlgztsbd ncqdr zmb rpcdfph qjsbk gzgvdh xnfhq hlmvqh cbbkfx knnmm qfkjsq xddkbd vgp pmtfmv qdpbx cnghsg hrfmdk fjgxv xlnn xjzc mszc ljmvpp zntrfp fdf pcf mnvq thvm bkd fbcds dbx fstgc dln pfqxsxd zrgzf mhrm pbn zttx zhghprj (contains peanuts, eggs, dairy)
nldzpc gmc mjpt knqzf rbvdt zntrfp nthhxn jmdg rxr xzcdnr kx ljmvpp kltcm jmgt gjqfj pgqxp xjrpr zmb qrsczjv hlmvqh dbx dmxhhd pnglkx gsgmdn vhcnpg zrgzf xjzc pjqdmpm rpcdfph lbfgp xgbvk jvvmcq qdpbx nqfc dvcfx thvm rknm kbtx npbnj mrxg klmjmz rrbndl xbpb ncqdr fdf vpvj kglr pptgt mrfxh (contains sesame)
tshn dmxhhd qmthj kqzcj rqqfnlc pcf dgrrm hkqp ckqq flhfddq qmmt thcs vqrjn vht tbm lqmfgp bcvmz fbcds jmdg rbvdt xzcdnr xlzqfb vfkpj mrfxh sdccxkt fstgc fhtsl qfvfzg kmsh dznd zrgzf bxv glrc thvm pmtfmv rkzhxmh zqsc xjzc fmvvb ddbmq qspfqb tjsdp rcvd xgbvk gzgvdh cmnb pptgt ngqh xlnn sjgx mrxg qdpbx rknm hnmjfl szsbj zntrfp gtgrcf fdf kltcm vhcnpg zmb pjln mppf dnpgcd ttxx qrsczjv srgnx qszmzsh (contains shellfish, nuts)
"""

from sympy import Symbol, Or, Not, And, satisfiable

import re

FOOD_LIST = re.compile(r"(.*) \(contains (.*)\)")

def parse_input(text):
    foods = {}
    for line in text.strip().splitlines():
        m = FOOD_LIST.match(line)
        i, a = m.groups()
        ingredients = tuple(i.split())
        alergens = tuple(a.split(', '))
        foods[ingredients] = alergens
    return foods

def create_symbols(foods):
    ingredients = set().union(*[set(i) for i in foods])
    alergens = set().union(*[set(a) for a in foods.values()])

    return [Symbol(f'{i}_{a}') for i in ingredients for a in alergens]

def create_clauses(foods):
    clauses = []

    ingredients = set().union(*[set(i) for i in foods])
    alergens = set().union(*[set(a) for a in foods.values()])

    for a in alergens:
        # Every alergen is in exactly 1 ingredient:

        # Every algeren appears at least once
        for a in alergens:
            clauses.append(Or(*[Symbol(f"{i}_{a}") for i in ingredients]))

        # Pairs of different ingredients with the same alergen are mutually exclusive.
        for i in ingredients:
            for j in ingredients:
                if i != j:
                    clauses.append(Or(Not(Symbol(f"{i}_{a}")),
                                      Not(Symbol(f"{j}_{a}"))))

    # Pairs of different alergens with the same ingredients are mutually
    # exclusive.
    for i in ingredients:
        for a in alergens:
            for b in alergens:
                if a != b:
                    clauses.append(Or(Not(Symbol(f"{i}_{a}")),
                                      Not(Symbol(f"{i}_{b}"))))

    # Alergens are not in unlisted ingredients
    for I in foods:
        for a in foods[I]:
            for i in ingredients:
                if i not in I:
                    clauses.append(Not(Symbol(f"{i}_{a}")))

    # # Make sure every symbol is included in the clauses
    # symbols = create_symbols(foods)
    # for s in symbols:
    #     clauses.append(Or(s, ~s))

    return And(*clauses)

def solve(clauses):
    return satisfiable(clauses)

def get_no_alergens(foods, solution):
    ingredients = set().union(*[set(i) for i in foods])

    no_alergens = ingredients.copy()

    for s in solution:
        i, a = s.name.split('_')
        if solution[s] and i in no_alergens:
            no_alergens.remove(i)

    return no_alergens

print("Day 21")
print("Part 1")

print("Test input")
test_foods = parse_input(test_input)
print(test_foods)
test_symbols = create_symbols(test_foods)
print(test_symbols)
test_clauses = create_clauses(test_foods)
test_solution = solve(test_clauses)
test_no_alergens = get_no_alergens(test_foods, test_solution)
print(test_no_alergens)
print(sum(i in test_food for test_food in test_foods for i in test_no_alergens))

print("Part 2")
print("Test Input")
print(','.join([s.name.split('_')[0] for s in sorted([s for s in test_solution
                                                     if test_solution[s]],
                                                     key=lambda s: s.name.split('_')[1])]))

print("Puzzle input")
foods = parse_input(input)
# print(foods)
symbols = create_symbols(foods)
# print(symbols)
clauses = create_clauses(foods)
solution = solve(clauses)
# for sol in solutions:
#     print(sol)
no_alergens = get_no_alergens(foods, solution)
print(no_alergens)
print(sum(i in food for food in foods for i in no_alergens))

print("Part 2")
print("Puzzle Input")
print(','.join([s.name.split('_')[0] for s in sorted([s for s in solution
                                                     if solution[s]],
                                                     key=lambda s: s.name.split('_')[1])]))