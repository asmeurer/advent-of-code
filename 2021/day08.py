test_input = """
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

input = """
gea agfcbe egcbfd aecb cegbf cafgde fgeba ea gabdf begfdca | bcfeg ea fbdga fbgcdae
gbcd gce fedgba edafgc cafbe febgc febgcd cg egbdf dgcefab | ceg cfdgae bdcg cdgfbe
eaf cfade afgebc cdegfa abcfd feagcdb dfbgce ae dcefg dage | eaf cdgefb fea bfacd
faegbdc fagcde dbcfg ecgfb afegc gbe abec bgfcea eb befagd | afcge egb cgfbd bace
caegb fcaged ce gafcb gfcabe egdfcba acdfbg eca dbgea bcfe | gedbcaf ec ce fegacbd
bcegad beag agcbd ged degcabf dcaegf fecdb eg dbgfca dgbec | gcdebaf gde bacgd egcdaf
cbgef cgedfa agedfb dfca dgcef gbedac faged fgaecdb dc dgc | aedfbg dcaf cbdega bgaefd
dgfabe bfgce bfgea cdgefba fgbdca cefabd ae bae fgdba edga | ae fbgea dega ae
gdbefac efadgc gcbdfa cdgeb baecg bga agefbc gfaec ba feab | bfgedac abg cfgbae ab
adfbc ea eabc ade dcfeg cfaed abdfce bedafg ecfgbad bfcgad | cfade fbadec eda bgadfc
efgda dgeabf decbag acefgd edbfa baecgdf ba adb gfab dcfeb | agbf abd gdabfe ab
acbefg fedacb abde be gaedbcf agdcfb bec cfedb dfcab cfged | gabdcfe bceadf fgbdeac fegdc
deagfcb ebadc cgdea gacb ebgfad ba bfedc eab fgeacd bdcaeg | ecgad abcfgde gbdeaf dfbce
cbega dfaeb fcgbad gf ecagdb aegcbf gbafe gfce bcdeagf fag | bafge gbfeac fecbga gcafdbe
bgd efabcg cafbgd bfdgeca gdfe cbgfde cebad bfceg gd dcegb | egfd ebfcagd egdf adbec
dgbecaf dgcafe bedafc fb afgbec bcfda dabcg abf cafde dfbe | abf gacfedb cedaf ecadf
egfdcb afdcgb abcfedg gac ga fdgcea acfbg bfeca gbdfc gdab | befcdag agfbc eadbgcf afceb
gfdaeb gafceb ecdb fcdaegb acfgd cgeab ecgda abdgce eda de | dcbe dbfgeac gcbea baecg
ega bgdafe gafbcd afgbc abced baceg cfgbead fgec eg agfbec | eg dbegfca aeg fgce
dfbacg acbdeg afg bedga gf efgd eabdgf bcafe fagbe fbacgde | egdba fag cabfe gfa
dfbgeac feadcb aefcd abefd ebfdg gfcdae beca ab cdafgb bfa | abfed dbaefc cdaef dbfgac
ecgafbd gbaecd bfed fedbca geabfc de dfeac dae fgcda fbeca | acbdef acfbge bcfea beafc
adb bfedac cagdf eacfgd gcdbefa ecgdb gbaf abfgdc abcgd ba | cdgab acdgf dab ab
aegcdb ag bdgef aefcbd gbdae gacd aegfbc cgdbeaf dbace bga | gba dgca fbegd fbdge
cgea fdbega cfagd dae feacd bfdec ae fcgbad egafcd aedgfcb | gace agefcdb caefbgd ae
egfc cae gacbfe fdbae ceabf ce cgedab fdgcba fdbaegc fbagc | egcdfab cgef ecfg fgcab
bagcd afgdcb cdfa dcebfg fbcaedg bcefga ac dbeag fdcbg cba | ac cfgbd ebfdacg acdf
abgec bcaed bcaefg dafcge fdecb dabg ead ad gaedbc acdfbeg | ceadgbf bgda bagfec ade
acgde fcg acgebd dagfc bfdac adcefbg gf dgbcef feag dceagf | bcgdfe fcg fega gf
facgeb bfacg dabefcg cdaebg ec edbaf ecfab fceg cae cdbagf | cae gcef adefb facbged
gfeacd gbecad bce cfgba eb daeb efbcgd agcfdbe bagec dgcae | ecb eabd bec egbdfc
faegd agcfe bfad fd fed abfgdec gbadce edfbag eabgd cefgdb | fgdeabc df edgbfc egadf
dfeag efgadb bagdce bfcgde dcbagfe bgdea ef acdfg bafe edf | aebf fde def egdba
dab aebf dcebf dbcegfa egbdcf dacfb ba cdfga fbdaec egcbda | ab bad dfacg dgafceb
dbf agfdcb cdbfeg cadbe fd bafcg ebfcag egfdacb dfga bdcfa | fagd df cfgeadb ebfacg
edbaf deacg adcfbg fgecad beacdg acb abecd fbegcda cb cebg | debca daecb eacbd acb
ebgfac egfa dbacfeg afebc abcfdg cdefab gceab agc dcbge ag | gac ag facgebd egaf
bfdage bde bagd badfe ebcfgd afegd fdcebga afbce aedgfc db | gecfabd dbcgafe afgcbed db
dacbeg aegbcdf aedcf cg bagef gafec ebgafd bgcf gca cbeagf | cag bfgae gbfc daegbcf
fceg bcedaf ecfgadb cg begfac eabdg cbg eacgb dbcfga ecbfa | agceb baecf gc dbfaceg
egdf dacfbge eg gce acdbeg dfgcb fgecb fbdgca gdefbc efcab | ge bfedcga abcdfge fbeca
cefab bcgf cg fgead ebcfad dbecgaf bdgeca eagcfb efcag cga | gac adfeg cga gfbc
cfbgd efabcd bagef da bgadcf gbfda bdcegf bda bcgdafe gadc | dabfg da bgeacdf dab
feabd bgd begc edbgf edcfg afdecbg afcbdg cgefbd gb adecgf | befdg dgefcb dgecf fdgec
cdegba bdcg fecad bdaeg dbagfe bce gcebaf cdbae baedfgc bc | ebc cb edfac bfgacde
gfc ebdgaf cbfdge gcdaef gc fcdegba degfa eagc cfdba gfacd | gdfae agedcf fdageb fcg
bfgdc cafedbg eadfcb fgdace cbfda acebfg ebad ad acfbe dca | da ad fcedba acd
agfeb gced cdgebaf bcadfg gedacf dag gd agedf edcbfa eafcd | dg eacdgf dg gecd
edgafb bfa eabgc fa cbaedg agcbf gcfdb gaebfdc baecfg efac | abfegdc gbadecf cefa cagedb
gdaf defcb bgdaec cefgdba fg bdfeag becafg gfe eadgb bgdfe | gfbde gf gf acbdfeg
dabgce cebgfa egfdb geafc eda egadf cgfdea fedagbc dcfa da | afcge eda dae ad
adcef cegda cfa feacbgd dafbgc befdc egfa fa gbecda dagefc | geaf baedfgc fdeagc bdcega
gdecfa ecadg cgfd dc efbgac cefga feadbgc dca gabed dcfeab | acgfe gfdc dgfaec dca
cdbag aecb ca bgecad dac dgbfc debfga adegfc abdge adefbcg | dac cdgba gedafc ac
cdbfeg abe dbcafge eacfg ba cbfde bcafe eafgdb acbd fedbac | fcbdage abe eab eab
gdafc defgbc fdgab eafgdbc agfce adbc dc fbacdg gedbfa cfd | abfdg gfadb bcda badc
afcdge cafde acebf fabedc fbedagc cdeb fgcabd cba baefg cb | adfgbc cgedafb abc cba
gb agfbd deabf gab bagcdfe agcdf cfgbae gcabfd agcefd dcgb | cafdge gbcd acdfgeb cgaefd
gbadcfe ecfgba ebfad gabcf ace ce bceaf cbge gecdaf bcadgf | begc bfgac bafgcd gcbe
cedbfa bdecgf gfcdbea aecbgd gbcaf abgdc gd edga gdc cdeba | abedc dcg edga dcg
dcage fegcbd cdab gbfae ebdagc gbfdace bd baged dbg cfagde | daebg dcbeag efabg dbgae
agdbf gfac bedcafg cbafd bafcgd ceabdf fbcegd dfg gf dgeba | fg fadbc cfgebd gf
ab cagef fgeacb bag fdcgb cagfdeb eabf bfgca degbca edgcaf | fcbgd edgfac cafgdbe gcfab
befdg dafbeg dfbacg ge cdegba gfae deg dbcfe dgaebfc gabdf | eg eg efga bdefc
beafcd gbaedc adfecg afbdecg bafgc ef dgeac ecf aecgf dgef | dfeagc cgdea fdecga fce
degbc agcbd ecabdg bcefd gfdacb eafbgc decgabf gdae eg gbe | gcbda dbefc dcafgb gcfeabd
bedacg bge bg cfgdea bcedf gaedc dbceg fdbcgae dgab gecfab | ecfbd egb beg adgb
bagdfec fdcb gdbeac facbg egfab gfc fc cadfgb geafcd abdcg | cbfd adbgc fagcde dbceag
afd fa fgbaed facb decfa dbeafgc aedfbc fbgdce cdage decfb | afd cbaf eadfgb caedf
fgead dgfbac df gaebfcd fgd gedab cadgbe defb gafec edgafb | badegf edfb fdg fgd
dbceag egfc ecadf degcbfa eg bcefad ega egfad dfbga fcegda | aefgdc defga ge bcaedg
dbgef dcfeb dcba ceb faecdbg adcfge bcaegf adbfce cfead bc | bc dagbecf bc bec
edcb fbgcd bgefd fgabec dbagfe cb dfcga gabcedf egbcdf fbc | afcbedg bgaefc cb egfdb
baefcg ad fagec acedfg agdf efadcb fagedcb gdcea dac gbced | cbegfda gfdcae fadecb dac
gedfca acbdgef egdac gafbe acegdb aefgc cdfe cadbfg fc fca | caf cbgfdae cfabgd cfed
agdfc ebdgac eafdgc degca af cdegbaf efca dgfcb bdfage fga | cegad gaf befadg dafgc
cbadef dabfge caedb feac adgcfb ea bacfd eda deafbcg gbedc | ea gacbedf efac acef
eb gfadbe dcefa gfdbc edcgfb cgfdba deb bcge dgbfaec bdcfe | fgbcd egcb ebcgfd bgafdce
adcbf bfaed cd fdec gcbfa acd agcebfd cegadb afbdge dceafb | dacfbe dac afcbd bdfca
dba gdcfbe ba gafb gfdbaec gdcba aedgc afcebd gcbfd dfcbag | ecgbadf faebcgd decag adb
adfgbc eabdgc gebf efdca eg bcfeag fdbceag cafbg gec fagce | gabcde cge abfgc fbacge
gb fbeagd dfacb egbf aecfgd degfa ecgbfda adecbg bga gdabf | efdgba dcfab ebdcga dfbga
agfde efdgcb aefbcdg dgbfe dcafbg adbe dbafeg fda da cgfea | dfa geafc ad afd
ab bfa bgfed agfdcb abdfg efcdab dgeafc bacg badcefg facgd | edfgca gdcabfe baf acgb
agfec befc begdac bcagf eagdfc gdbfa cgeafb cfebgad bc gcb | fbce cebf fabecg abcgf
gecadf dgbfca gfabedc aedfgb cdgba badfg cg cdg bedca bcfg | cg gc fcdagbe bdfag
cag acbdeg fdabegc gcfdbe bgaf ga cagfbe cfeag bfgec feadc | gbfaec fgab gfcae cgebaf
febcga gbfc edabcg gfabdec fecdag bg gcfae efadb abgfe gba | fabge bgfdeca bag afdbe
fcdae gabed dbcea bcgdaf aefdbg gcbe bdc cb aebgcdf acedbg | dgbafc bdc gdbefa fadce
gbecafd cbaeg cefagd aed bdag acedb efdcb cegabd efacbg da | gbeca dabg da edcfbag
gfdeab defgbc dfagb bgc afdgcb efabcgd cb acfb agcde bdgac | bc aefdbcg aecdg bgcaedf
fabedc fdeac fbd adfbe bcefagd dfcgbe dbage fb fbac gaefcd | afced fcab dfb edbaf
aegfbd befad cbgea dg bdeag fedg dga fecbdga cabgdf bdfeca | dafbe acdbef acebfd gfed
becaf ecbfdg begcaf dcbga deb dgfacbe ed afedcb afed bdcae | aefd dacbe dfbace cdbefg
cdgafbe bgecfa da fcage dfa gcfead debfc gfdbea cadg cdeaf | adf cdefb febdcga fgeca
dcefa agbdfc gacfeb fdbcea bedc dc cda cabegfd defga becfa | cgbfead adc dca cda
gbdeac beafgc fae bdcef cgeba aebcf aefbgdc fgdcae fa fabg | bdcfgae fgdaceb af cbefa
gfdabce acbde abgd fdbceg ecdag bd becfa edcbga bed fcgdae | ebd gdba db feagbdc
age gcbed gcbea dbcgfae acde fcabg acgbed ebfadg ea fcdbeg | cade eagdcbf bcgeda daec
afgbcd edfcg dcf fgbade cegbf dc afegdbc adce efdag fgeadc | dcfegab gedabfc dagef fcbeadg
gdefc dac afbceg feabdgc aedcg bcadeg da cgbae bagfcd abde | da ebda gbaecf efgdc
fgcebd af abefcd dfceb acdbf fda dafgce dcgefba afeb acbgd | cgdba decagfb fad af
egfba agbed ade dfab cgebd agbdef aefcdbg da cbgaef cgdeaf | fdbgcea ad ead cbeadgf
eda abcgfd afgde fagdcbe gdfec ae debafc afdgb ebag afebgd | ea baefdg fgeda ae
eg gdeaf bgfe gdbfae agdfb gea bafecdg defca gbdafc bdgeac | cdfbga fbgda age eg
dbafce daegb eadfcg efadg facebgd df cfgea edf fcgd efabcg | gdeab fed efcag ecgaf
fbcea gbafc fae ef daefcb eacdb cdfbega dbfe gbdcae fadgec | cebaf gfcab afcbg ef
gbdefc edbag cdfaeb bc cgbafde cbdea efacdg dbc afbc cfdae | aegdb gdabe bfca fcba
cfbegd gbcde fgcdb df efgbda fdce bfacgde fbd dbeacg fcagb | df dfabeg fd eabfdg
fcdeba cad dc fgeabd dfabe dbecagf acdef bcfd fgcae gdbeac | bfadgce afdec gdfeab edcfba
afbdec febdg befcg debag bdgefa egdbca df bdf gdaf bcfedag | fd dbf cefgadb degba
gbaedf eacdgbf gebac dbacef eag ecbgfa eg fcabe ecgf dgbca | bcgae ge ge gebac
defb facdb fd cgeabd eafdbcg ecfgda cdf ceadb bafedc cgabf | dafecb dbfe fedb fdeb
cdeab bcefdg bfag fbdeag dafeb eafdcg dbgfe gefabcd fa daf | fda adecb ecdfbag adf
dcfgba gbca acdfg fbcgd agecdbf fdcebg dacef efdgba afg ga | afgcedb cgba ebdgfc efabcgd
dfcgae baf cgefa agecfb beag acbfe defbc ab cadgbf gebafdc | acedgf ba gfcadbe afgecb
agebdc eagbdcf fgeabc adfecb defga dc beacg agced dac dcbg | acd geafd dc ecbadg
gbaedc agfec dacef efabgc cgfd dc dfeba dac eafgdcb aecdfg | geacfd dac dc ceagbd
bdafe dacbgf edcg gedfcb egf eg agbdcfe gbcafe bfcgd fbdeg | dfeab abgfced gdec dbfecga
abgfc becgfa cadbfg fega cef fegbc dbeacf abgdefc ef cbedg | abfcdg acefbg bcaefg cef
adcfe dgec ecdgaf cgfbead eg fdbcea degfa eag cfgeab dbagf | ge edgc fgecbda dcbafe
fcebad eagcd cfbe dacgbf egbcfda fbaed fdc cf gbfead eadfc | abedf fbdaec bfaecd cbef
afbde abg bcfead cdgeab gfeb gb eafcdbg gfadb efadbg dfcag | gadbecf gb aedgbf gdbeafc
gcb edagc gb gbdf dcgbe bfced gebfcd efcdba cfegbad afbcge | gb bg adceg gcb
cfdbgae cga cg dgcbea egabfd cefg fgaedc cfabd dgcfa efagd | gac cebfadg adfegb adcfeg
cbga aefbd gb adcgfe edcbfg deabcfg bcagfe feagc febga geb | agbc cfeagd gbe dcefgb
dgfceb bdacg egda cdbeg cad bdaecgf fagbc cbedaf aedcgb ad | gade egcbd cafbg adge
bd degcbf bcda dfagbec aedfb fdage decbaf efacb fcebag bed | dcba dbegafc cefab bdfaec
bdae cbgdea gaceb gbfdc fgdeca dagfbce cda ad acdbg cefgba | da dbae dcgab da
bacgdf bdfca adefc bdc adcfgbe fbecga agcedb bgfd fagbc bd | fbdg bd cgdbfea cbd
bdeg fecbga ecbda gecdaf agdce abcfd ecb ecbdgaf eb cbaged | cbe aebcd gedb bec
dcgfba cfegab faebcdg bae cdfba badec cebafd be debf daceg | be becfga afdceb fbgadc
ebgcda begdf gbe ge cdbgafe dfagcb fdegcb cfeg feabd gdbcf | gdabec ebdfa ge afbed
dbcg cadfebg faecg dg gfcad fgadcb fbdeag dag fdcabe bafcd | fgdac gefca agd dg
dafcb agfeb ce bdgfac ebc acdfeb abfce cfde fedacbg begdca | gaebf debcfa bcadfe bec
bdac gbd bcagf agbfdc agcefdb fgbda bcgedf eadgf db facbeg | bdfag cfbgad gacbfe gfead
df dfagce cfageb fdbgce gfcadeb cfd dafe cfgae agbcd fgcda | dgbca fd fagec fcd
becdfa bfdca fgbacd gc dgcfb egdfb bcg cfag dcbaefg bcdage | cafdgb cbg cdabge cgaf
dacbeg gbdf dfebca df fagec def abedgfc fcedg cbgde fgebdc | cedfagb cagef cdgeab egfcd
edbcag edgbc agdbef ebacd cdeagfb bda ba cagb dface gcbedf | cagb dba dcbgaef adebc
egafbc adcfgb ef cdgfeb fcdgaeb ecdag cfe cdgfe ebdf dcgfb | geadc eadgc fec febcag
aefgb gac gabce fcgaed ebagdc gc cedab fdbcae abcgedf gcbd | cbgae dfeacg bgdcea agc
agcd edbafc fda ad fcaegd fegac adfgebc dfaeg bgdfe fgbeac | agcd fgecab ad bdfge
fbgecd dcabe eafgbc bef cegfd efcbd fb fdbg gfdeabc cadgef | fb cedfabg efgabcd bf
egfcba cfgd edfba fecgbd dg edfabcg gde gfbec fdbeg bdcage | dge fdcg gd cgfbe
eacdgf fdbga bgcefad acd ca fgbeda ecbfd bdgcfa abcg fdcab | gbfade gbafd gacb abfdc
abdfc afebcg edabg dcge gbdefa gbdca cbg cg dbgace bcgeadf | bgc bagefd gcb bcfda
gcde geb gabdfce eg bafdec gdcbae ceabd gdfbea bgfac gbace | geb abfcg cbdea gbfac
ge fcead edgac ged dcagb dgbaecf afeg eafcdg bcfade gedcbf | gfea dfgcbe afeg gde
ceb acdbe cb aegdb acgb cebfgd ecfad efgcdba feabdg cdagbe | cbga daecf cabg cb
bcgaf gfbea gea cabdge abefcg gabdfce cbgdfa cfea ea gbedf | age ae adgbec gea
cgdb fbgea cg fadbcg bdecfa abfcd gabfc gfecad cdfeabg gcf | fcg fdegbca gbeacfd cfg
cbfae bedafgc fbcgde agcbf bga faebgd ag fgabcd dcga dfgbc | efcab ebcfa dbcgf cadg
gced egafdc cfeabgd cfdae gecafb fadgc ec fagcbd cea afbed | gcbdfae dfgac cbeafg fdcgae
cagd dcfbg bfdec gd fcagb agedfcb bcgadf gbaefd efcagb fgd | fcadgb gd abcgf cadg
adbfc bcafe cd fadgeb gcfd gbfad gadecb dca ebfgdca acbfgd | acbdfg dgcf bfcagd dagfb
fcaedb eb bdfgcea dcafgb dafbc bdeafg befac efb ecfga dbce | fbcea eb cdbe eb
fdagce eca fecgdb edbgac abed dgafbce cegab cabfg bgecd ae | ebda cea dbcfge fgcab
agefdb ec afedg cbgaf daec dbcgefa ecfag ceg cgafed egcbfd | fdbgce dgfecab bafgde gafbc
bcega eafdcb abfgdc dacef gefadc bcd adegfcb fdeb dcbea db | ceafdb debf bdef eacdb
afb egaf fgaceb aecdgbf becgf acdefb af abgfc dcbag febdcg | fa fa cbgaf eafg
cagbfed cgdbe ag gbedcf aefbc gbeca gdba gae edcfag degbac | ecagb gebac begcdf ag
adf dgaec eabdcgf cbfga cdgaf fd eafdbg decf cfgaed ecbgad | fda fcgba dfa egcda
adfgce bdgaf agfcd dbeag cdfb bf fgacbe fcgabd fbg cbafegd | gedab fgaedbc fedbcga gbcafd
fedbga cefba cbd gbdea cabed ecgd dc gbdeca adbfegc cbagfd | cd acefgbd befca aecfb
agecbd facegd gefadcb gcaed geaf gcf dcbfe dgefc dafgbc gf | eadgcf aefg gdbcfae gf
bdgaec efadbg fcadeb dbegc agdc bcgef edagb aedgbfc dcb cd | bedag dcga bcd fdeagb
adfbg bfc cdgbaf dcab fdabge bfdcgea cbgaef cgdfb cb egfdc | bgafed cb cdba dbafg
gdbaec bge gbad efcbd egadc gfdcaeb bg egfcda cgdbe cbaefg | gcfabe gdba bg fgecad
cfdagb cgaf gfdab fa eabdg afb ebdcfa fbcgde gafcebd cgdfb | fa af bfa dacegbf
ecafgb cfedga abdcg debf dcbfea be bec dacbefg beadc adecf | eb faedc debf cbe
gd cafbgd efbga agd edafcgb gbadec cdeab edgc geabd cbfead | dga dg agd dg
abefdgc dfae dbfcg fa gabfce agf cebagd dgace dfcage cdgaf | cgdfb fdae efgadcb gdcea
egdbc cadf gfceda ebagfc dagec cgeaf bdagef gad ecafbgd ad | cegda eacdfbg da dfac
gfadc aced dcgbfa ae dfebg efagd fdeacg fbgeac cegfbda age | bfdeg cgeabf gea cead
bc bfdega fbc bgaef ecdbaf cfbgae acgb egdafcb gefdc gecfb | cbefg bfc dcfeab bcefg
cdebaf egcbf bdfgc adfcb cgd agdb ecbafgd gcdaef facbdg dg | bgad gcd fgebc dcebagf
eabcd abdgec agdcfb cdbga eb dafec bec dbeg cabgef cfgbaed | agdbfec dacbe be eb
cabfedg gbacf beca eb bfe afebgd efcdg cfageb cgefb dgabcf | be dgefba dgcaefb eabcfg
bdfga fbgcd gdfcab acdf bafdge cfg cfbgea fdagecb cf dbgce | gcf fgc cf cdfa
aeg agcde aecdb gbfdea ag gacb gafcdbe ebdafc gedfc ecdbag | gadce gea agbedc cedgf
bdg fdbge fcbd aecgdb dcgfe fcdgae fbage bd abdegfc ecbdfg | fcdb bd edbacg decgf
fagdbc dbc dbag cefdg db bcfga efdacb faecgb cdgfb efagdbc | dagb cdb cgdbfae abgd
fadecg cg bgcd gcefabd fgeab fadcbe gcefb bfcde ebdfcg cfg | bfedcga bgfcdea dcbg begcdf
fgacde dcegbaf fagbed ceab bfa aefdc cdbfa ab cbgdf bfcade | fba fceda baec bfcdea
dfeca ceab ebcgdaf cdebf bgaefd aed ea bfgdec fcdga cfebda | aedfbc dea deacbf dea
afdegb dabcg egd eacgbd cdefb egac eg gebcd ebfdcga bdafcg | agcbd fagdceb ecabdg dcbga
gcb bfdcea bg cgade bdfce bfgd dbegc cegfab befcgd dfcabge | efcbgad edgfcba fdgb afgcbe
adbecg cad fgacbe gfcda decf dc afbgd fgace dcegaf ecafdbg | acgebfd dc cda fgcea
egbfad bdfca bg dfabg bagdecf egab fagde ecfdag bgf fgedcb | dfacb gb dgaef fbdac
bfdgc ac fdabcg dgcfea cad aegfdbc cebfgd gbac adebf afdbc | ac bdgfc cgafdeb edbfgac
gbacedf cadbef gedc agcbf cbaedg cbade ecgab eg bgfade age | gdfbaec dcebfa dgfabe ega
egcdfa ba efdbga bgcefa agb fgcab ceagf ceab fdgcb fcdabeg | cfagb bag cbgfd fbagc
baced fcdebg gecaf gaebcf eadbcgf gfab ecafdg cfbea fb ebf | fb bgfa afecb aegdcbf
ebfadg cbdfaeg gcdfea agd da dcbgfe gdfeb bgeda dbaf ebacg | fbad da cegab abedgcf
cdfgeab gdbfa aebdf cdeafg gb acfgbd fbg dgacf egabfc cgbd | cbagfe cebgaf gcadfe bfg
dcgeb edgf dgfacb dfc edabcg df bfeac gdcebf fedcb gcdabfe | bafce debgc df ecbdg
fdb db dbeg abfegc dcfeb ebfcgad decaf efbgc fcgabd fgbecd | cedfa dafce cedfb fegbcd
afdc gbcaefd baefcg gdbecf gbafd df ebadg dgf fcbag dfcabg | fdg dcfa abegd df
af cegbfa bfca egdabf aef bgeac cfaeg caebdg gdecf gcfebda | ecgfd ebfacg bcage dcefg
"""

def parse_input(data):
    lines = data.strip().splitlines()
    splitlines = [line.split(' | ') for line in lines]
    signals = [(frozenset(map(frozenset, line[0].split())),
                [frozenset(i) for i in line[1].split()]) for line in splitlines]
    return signals

def part1(signals):
    return sum((len(i) in [2, 3, 4, 7] for signal, out in signals for i in out))

def disambiguate(signal):
    # Just solve the puzzle by hand.

    #       0:      1:      2:      3:      4:
    #  aaaa    ....    aaaa    aaaa    ....
    # b    c  .    c  .    c  .    c  b    c
    # b    c  .    c  .    c  .    c  b    c
    #  ....    ....    dddd    dddd    dddd
    # e    f  .    f  e    .  .    f  .    f
    # e    f  .    f  e    .  .    f  .    f
    #  gggg    ....    gggg    gggg    ....
    #
    #   5:      6:      7:      8:      9:
    #  aaaa    aaaa    aaaa    aaaa    aaaa
    # b    .  b    .  .    c  b    c  b    c
    # b    .  b    .  .    c  b    c  b    c
    #  dddd    dddd    ....    dddd    dddd
    # .    f  e    f  .    f  e    f  .    f
    # .    f  e    f  .    f  e    f  .    f
    #  gggg    gggg    ....    gggg    gggg
    d = {}

    # First the 4 numbers which have a unique number of segments
    n1 = [i for i in signal if len(i) == 2]
    n7 = [i for i in signal if len(i) == 3]
    n4 = [i for i in signal if len(i) == 4]
    n8 = [i for i in signal if len(i) == 7]
    assert len(n1) == len(n7) == len(n4) == len(n8) == 1
    d[1] = n1[0]
    d[7] = n7[0]
    d[4] = n4[0]
    d[8] = n8[0]

    # 2, 5, 6  is the numbers that have only one of the two segments from 1.
    # Of these, 2 has one of the segments (c) and 5 and 6 have the other (f).
    c, f = d[1]
    n2x = [i for i in signal if c in i and f not in i]
    n2y = [i for i in signal if c not in i and f in i]
    assert len(n2x) == 1 or len(n2y) == 1
    assert len(n2x) == 2 or len(n2y) == 2
    n2, n56 = sorted((n2x, n2y), key=len)
    d[2] = n2[0]
    # The other two are 5 and 6. 5 is the one with 5 segments and 6 is the one
    # with 6 segments.
    assert {len(i) for i in n56} == {5, 6}
    d[5], d[6] = sorted(n56, key=len)

    # Remaining are 0, 3, and 9. 3 is the unique one with 5 segments.
    assert len(d) == 7
    assert len(set(d.values())) == 7, d
    remainder = signal - frozenset(d.values())
    assert len(remainder) == 3, remainder
    n3 = [i for i in remainder if len(i) == 5]
    assert len(n3) == 1
    d[3] = n3[0]

    # 0 has e and not d and 9 has d and not e. We can disambiguate these with
    # any number that also has one but not the other, e.g., 4 has d and not e.
    n09 = [i for i in remainder if len(i) == 6]
    assert len(n09) == 2
    de = n09[0].symmetric_difference(n09[1])
    assert len(de) == 2
    D = [i for i in de if i in d[4]]
    assert len(D) == 1
    n9 = [i for i in n09 if D[0] in i]
    assert len(n9) == 1, (n09, d[4])
    d[9] = n9[0]
    n0 = [i for i in n09 if i != d[9]]
    assert len(n0) == 1
    d[0] = n0[0]

    return {v: k for k, v in d.items()}

def part2(signals, debug=False):
    res = []
    for signal, out in signals:
        d = disambiguate(signal)
        if debug:
            print(d)

        outval = int(''.join(map(str, [d[i] for i in out])))
        if debug:
            print(outval)
        res.append(outval)
    return res

print("Day 8")
print("Part 1")
print("Test input")
test_signals = parse_input(test_input)
print(test_signals)
print(part1(test_signals[1:]))
signals = parse_input(input)
print(part1(signals))

print("Part 2")
print("Test input")
test_res = part2(test_signals, debug=True)
print(sum(test_res[1:]))

print("Puzzle input")
res = part2(signals, debug=False)
print(sum(res))
