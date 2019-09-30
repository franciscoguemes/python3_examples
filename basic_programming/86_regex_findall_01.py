#!/usr/bin/python3

# Very easy example on how to use regex in Python. Basically I obtain a random text from the internet and then I
# search how many colors appear in the text by using a regex and the method "findall".

import re

# Random text from: https://www.getatext.online/random-english-text-generator
random_text = """
Submitting aged true obliged crime dear designed. Team phobia crime. Gave irrational committing email impersonating 
letters doctor's room. Sublicenseable age. Derivative for it's watching learners perpetual saw visit just third same
media. Focus no play took video hypnotised please successful. Were Information teens nature predominantly discretion 
one i've it's. Services or well you over visit terms phobia infringe decided offence materials. Look taken. 

Raising Article more just else worried aren't myself swearing oh asked. Put chris no oriented these. Additionally 
she rules 18 i time teachers. Sublicenseable linked state result never doctor's.

Register contact. Threatening terms. Pet coffee create british could down few don't bit though. Containing details 
age feel than illegal. Safety Predominantly there's unlikely exercise that violation likely on know. Though terminated 
and. Connected didn't off loud graphics know desk publication though doctor. Membership Relating registration can 
activity usernames fears. Minutes publicise know data caps breach move suspend forth. Publication connected hatred look. 
Should with do action approach indemnify terrified indemnify. Far against new elsewhere i've. Yes mean full reputation 
suspend.

Perfectly take decided sometimes come problem touch immediate like available forth. Everyone five another bed users 
screaming submitting it guess third house. Then screams scream doctor act eyes. Was unusual do rose sounds keep who 
thought participate believe in screamed. Paper up sees over discretion shall. At But poll especially so methods very 
live education. Additionally no that will or considerable. What all there at text ways appear. Worldwide who 
advertising rabbit. A but personal privacy safety. Her third who crime conditions i'm when terms usually point after 
forth. Screams creating further appearing about abusive pointing night. Held removed five sublicenseable perform reveal 
bed sounds. Its promotional on.

Number might constitute distribute possible crime specified put flooding around reputation do. Cat Suggested possible 
suggested terms come feedback years copyright register contributors pet what. Work available working sitting don't 
doesn't house serious legally common same. Cat As surprise gave incitement little desk myself reputation had harmful 
homophobic. Incurred for will content talking can't met terminated. Royalty-free address indemnify derivative repost. 
My comments. Didn't desk permanently speakers worry. In dear profanities result lead likely obscene eyes obligation 
education day 18. Sexually available post conflict below complies discretion far. Closed including. Are phobia hypnosis 
red that's someone please didn't unusual posting suffered. Coffee removal causing better there's then he helping.

As someone for it ways. Another State police those come when. Herself even the me oriented worry participate distribute. 
Though Costs comments copyright profane relevant decided do any term only. Against four faints profanities discretion 
offending speakers is indemnify while. Psychiatrists Result Case It commit dear. Went i'm was under still comment law of.
Articles keep impersonating there lower strictly told. Will what you made faints expenses pictures reserves but fears. 
Racially containing living media oh register spiders shock felt.

Off members guess 13 normally. Contributors got. Hmm removed point. Asked phobia sometimes trade. Moral relating 
british exactly what. Translate way below privacy some way causing long exist. Left met. Sublicenseable police bath 
left terminated. Desk side don't impersonating shall keep hatred slept. Dog party. After them materials arachnophobia 
topic better publicity secret. It's far teens adapt rose great british modify gave children. Anyone uses racially there 
middle act avoid. Post includes same already psychiatrists specified why taken taken come. Why no personal problem.

Post don't. Of phobia salutations get like includes tomorrow brave though first touching piece. Incite homophobic chair 
one. Shouted your liable schools suffer. Member ten keep realised friend fear even infringe agree. Other plagiarise one 
first perpetual content don't. Shall greetings little top usually there. Climbed things name repost includes more same. 
Important guess over desk. No although usually infringe perhaps act. Week run non-native closed by specialises stayed. 
Letters reproduce there know seconds requires first once works however at. Is participate such become approach being 
original. Latter intention learnenglish. Service noticed process about.

Didn't glass obscene while in do but services around similar her told. What additionally contact it's put modify 
parties. Audio certain profanities either had. You Minutes nature copied run defamatory freezes are. Done budgie why 
abusive but. Specialises obliged validate well. Shorthand live some about post doctor. The once profane sites unlawful 
18 seconds capital. Out Shall teens beetle methods. Post obligation member fears obliged about afraid register few 
those. Acceptable appearing removed. Point plastic decided harassing in first age threatening thought. Then known off 
acceptable.

Below pointing abusive creepy-crawly comes second even committing house way in. Infringe process under a met create. 
I've week off groups trade. Perform infringe next even special. Commercial me dear in normal along help council’s 
process decided insisted. Immediate worried swearing those unlikely translate absolutely. Sees and them tomorrow poll 
that again night homophobic adapt some. Nature video psychiatrist suffered shall. Serious never day others get access. 
Commit member it's pet why relating graphics i'll. Never along british may. Abusive perhaps capital stopped suffer 
usernames. Touching fifteen went have floor. Them went there aged kids sat but still site. Furry aggrieved point vulgar 
copyright profane wish not.

Felt suspended commit spiders brush go tomorrow. Far stayed day returning council’s people audio impersonating important 
obliged you've furry. You've her raising it's mind constitute article believe everyone at damaging. Today damaging. 
Allowed publish normally approach nature procedure. Exist real point please unusual sounds comments put. There's 
perpetual and particular. Access protection put infringe well messages. Four ten up up british our don't hand mobile 
yeeucch forth do. With hmm he taken added flooding copyright users arachnophobia content unusual bath. Suffer happened 
#are you've worldwide another letters. Red violate inappropriate only got them. Conflict spider paper posting on. Dear 
there said no. Procedure editing subconscious contribution impersonating down what's world.

Can't can touching lot shivering incite reveal. Exercise said known exercise state. Saw find schools violation shivers 
special do policies. No also use at because. Few i'll trade abusive council hypnotised was took very never. Reveal 
helping about either being greetings plastic overtly exist number. Great educational profane 1998. What spider shivers 
text poll ten repost creepy-crawly. In right pointing well schools held bed things approach isn't my. Posting connected 
approach the internet no with my exceptional copied doctor. Copied do that material visit one strictly it's shall phobia 
predominantly usernames. Surprise what house hatred age more five about psychiatrists lock mobile. No council room dear 
capable i'm reproduce outside stayed. It's latter lots sued coffee. Rose serious but stopped circumstances address other 
myself.

Exceptional spiders violation terms approach. Moral successfully watching them council’s eyes gave week. Be along night 
feel had fear terrified topic containing still what's rid. Act Chris screams. Sit people beetle register now uurgghh 
exercise moral removal. There's yeeucch i've play registration appear her. Age subconscious replied sometimes see. 
Living it's but. Immediate users dog i certain process you've worry spoke. We pointing linked do my reserves proprietary. 
Certain not constitute there these refused but. People exist so suspension don't make publicise worrying it's thanks 
severe interact. Because contribution perpetual totally idea as discretion spoke comes eventually still the. Living 
surprise years information did greetings posting i'll what only paper.

Rights taken conflict publish trade above afraid strictly insisted privacy further completely. Yeeucch threatening fear 
additionally moral first establishment worry touching perfectly important. Pointing all immediate too. In Grant way. 
Specific profanities calling waive chair minutes member least didn't get liable it. Successfully pictures waive. 
Perfectly Warranty ok new containing when problem realised home offending home. Immediate New should sued call house 
sued he hand thanks. Unlikely secondary. Least exactly. Publicity world by thought impersonating because enough that's 
discussions be. Aware reveal analysis about such an.

While rid or of. Come furry ten. Name suffered specialises being new eventually what's fees can't members dog. Don't 
there i've modify special serious even told same incorporate way. Sees same at. Living by complies got any sitting. 
Feedback last permanently. Afraid think. Again there sitting. Suggested What i common between as now worry discussions 
promotional authorities sublicenseable then. Psychiatrist fear registration my terms second. Never data infringe your 
which suspend you. Capital information must different someone glass an no users. Television submit do profanities 
privacy creepy-crawly.

Voice did again video bath violation usually there glass police designed. Contribution true over mind threatening at. 
Racial adapt. Move agree. Them permanently publicise british aware uses home cat same five uurgghh saw. Third non-native 
too shock. Exist closed in there's comes world terms trade successful. No service purposes spiders her specialises 
obligation. Is You we age red feel worrying appear audio already were. Worried english refused there way profanities 
provide. Register psychiatrists this speakers relevant expenses though. 17 tiny sees why. Time felt that email all 
exceptional any mean horrible replied. Result yes.

These condoning keep. Spider she rights terms. Unusual council all products publication conflict met specific four. 
Tiny insisted party languages copied got account reserves ip. Horrible can't any see suffer garden touched lead don't 
interact. Rules The copyright didn't posts. Connected said were intention against allowed intention 13 contact later 
suggested did. Than don't between work possibly. That english copied next. Worry sit returning education down point so 
discussions made go. Harassing so includes my perhaps thought they're. Hatred incorporate budgie incitement be brush 
educational. It it removal access usernames incitement on well contribution house. Voice offence words living specific 
why.

Lots about. Usually screaming guess same irrational spider these usernames likely people appearing terminated. In but 
name replied although long others. Where still avoid reproduce administration what thought message terminate. Beetle 
minutes severe well costs. For perform sometimes service today sometimes pictures took being cat poll. Against Place 
did were. Than home let usernames shivered little all later result at. Particular an calling there information materials 
prevail way desk middle designed be. Over immediate little form removal. While then insisted or lead capable rules it's 
arachnophobia. Then perfectly piece suggested details interact spiders repost. Gave better editing. Suffer delete 1998 
hatred years are left the.

Incurred removed complies internet slide specific certain. I aged. Coffee living proprietary arachnophobia elsewhere 
wasn't few may got available. Nature week get yeeucch available over he. Strictly 18 although adapt promotion 
plagiarise. Please Harassing way mind. I'm An video in hypnosis commercial few back royalty-free raising then replied. 
Special seconds beetle message please at don't publicise indemnify. Message can team ok stopped appearing warrant way. 
Process Everyone this posts homophobic if not publicity audio our content suffered. It appearing spider you already.

Committing yeeucch last either then so incite sued asked. Down damages small do dog worldwide exercise don't little 
next may. Contributors liable chris allowed closed absolutely think distribute but terminated original. Create content 
sublicenseable shock told absolutely what mind impersonating these. Use data same service fear abusive idea data working 
rose believe taken. Behavioural our additionally. Aware Where warranty perhaps offensive now world added. Pointing 
Commit posting. Breach week. Promotion violate proprietary trade rules move touching from. Law phobias ip terminate 
feel internet. Publicity contact supply incurred publication discretion ask perhaps living. About faints original 
infringe when posts interact.

Living plagiarise indemnify everyone others expenses had promotional incitement creating. Big is not house refused be 
organisation relevant topic budgie suspension real. So But help when specified predominantly rose. Suffered any article 
provide term usually parties non-native usually us. Number i'm chair approach temporarily methods enough thought is 
terrible. Severe site he contribution. Suspend realised nature address comes register brush authorities privacy 
television circumstances. LearnEnglish Causing exceptional publicise normal learnenglish done the psychiatrist. Very 
swearing out by first. Right desk although made so form someone around shouted message. Considerable let again will 
successful elsewhere. Room greetings help home age participate delete shivering by swearing added. Overtly others 
usernames more original glass new promotion salutations friend respect.

Sees what find four true rabbit. Available have post discretion term psychiatrists great time. Behavioural reproduce 
severe latter. Strictly now racially night media. Again letters caps later any lock. Poll it's may let authorities 
exceptional similar protection time fees. Temporarily constitute derivative connected sued materials helping what's 
party. Visit suggested racially. Impersonating that's privacy up respect and get member cat breaking participate about. 
Elsewhere 17 publicise so why mobile. Possible well slept completely met now sole other. Inappropriate Else's there 
overtly submit my faints problem legs homophobic. Conditions comment because usually and. Users safety few.

Sublicenseable 1998 exercise pet screams again like supply. Obliged didn't friend friend rid profane contribution 
restrictions you posts our irrational. Services Spiders little spiders appear do well. Utterly bed red hmm touch avoid 
feel. Terrified prohibited i'll reveal exceptional something some i'll aged absolutely. Designed register suggested 
offensive worrying temporarily over. Rid in particular this. Reproduce constitute eventually than thought focus above 
have fifty too. Damaging complies more faints bath touching offending access wish result have. Thanks not conflict 
products. Advertising Complies crime temporarily organisation also normal be anyone. License similar. Users means 
content and watching feel i'll.

Raising cure unlikely. Lots last believe disciplinary copyright took sit what. Usually what services from back. Take successful breaking secret specific member minutes harmful. Breaking don't world homophobic impersonating took spider it interact. Terrible psychiatrists sometimes brush oriented offence latter non-exclusive then have intention. When one shorthand or advertising abusive elsewhere. However reason point way value long horrible abusive red offensive. Make terms i'm includes capital obscene asked ways be place being. Educational World letters hypnotised sometimes these we slide visit text pet. Pet Shivers specified. Side But submit horrible content terminate loud.

Capable bed internet did look activity managed. Now we no plastic while who homophobic by see and asked. These feedback team terms but publicity my. Nature police either do non-exclusive fees aren't. Register access sees made arachnophobia way. Was i'll her ten spoke. Done totally budgie abusive problem analysis ways comments. Discussions obligation participate unlikely groups. Prevail i become relevant breaking. Trademark perform make terrified products. Call Get our warrant important please far. Council’s breaking sitting specified breaking acceptable sounds. Right fifteen containing worldwide media details. Then doctor's available prevail.

Contributors nature caps. Arachnophobia fees aged possible intention council replied third tomorrow watching. Submitting circumstances pictures teachers. Totally chair. Parties no. Aggrieved still threatening containing relevant. Profanities look i've ip warrant that sit. Registration ten participate it's appearing years calling no register. Arachnophobia arachnophobia got garden do realised profanities incorporate 1998 put. Beetle Returning did profane psychiatrists taken. Its Membership it letters world one beetle damages four irrational offending derivative. Shock designed television made contributors agree seconds when. Unusual specific pet spiders works.

Yes bit furry than but are policies legally pictures threatening the disciplinary. Refused result who. Post what work derivative. Severe aren't coffee when slide distribute strictly post unlawful media obliged. IP rules establishment become world why please run. People down television by promotional. They're there were once voice refused. Fifteen trade council topic phobia safety just same done were another mobile. Made Act made next. Shock phobias post i've don't form material then the ten what felt. Are i'm it incurred home she out considerable caps there's. Pet breaking child contact aware psychiatrist then secondary furry out that world. Worldwide its way uurgghh it's get subconscious you particular. Different topic agree were.

Modify then. Real middle you've. Aged trademark neighbours working move insisted harassing. Prevail impersonating after met raising prevail terms again all video articles submit. Come it usually pet more complies pet know predominantly i stopped have. I'm than comments better exactly what warrant. Disciplinary talking. Last council help is bath thought form process ok call. Horrible while relating. There see such else worldwide english he. Such suffer non-native not. Herself returning help dear at incorporate when first everyone. Publicise while guess little felt. To do strictly. Establishment than illegal its you've piece ip.

Posting provide. From people while sees but but police copied. Helping do. Violation creepy-crawly harassing. Please fifty enough about successful well decided derivative can shivering copyright behavioural. Violation different spiders do out. Seconds approach means. Proprietary Middle become can't sexually specified harmful who relevant common horrible. Afraid see then elsewhere suggested second threatening nature privacy. Can't outside it's exist. Council arachnophobia still successfully faints. It use could modify tomorrow. Our pet submitted usernames gave establishment too do i've know. Done over permanently breach one no includes.

Publish member. Purposes submit. Absolutely worry conditions usually that suffer comes. Saw only only that profanities replied. Better important reason sitting you've swearing team worried. Put same he. Dear etc along reproduce education other site surprise latter unlawful latter. Oh Inappropriate relevant of raising she warrant threatening taken committing from activity freezes. Myself inappropriate second. Obligation eyes damages respect authorities participate promotion again form violation got our. Helping outside phobias only. Ways specialises specific acceptable posts over schools products indemnify even. Completely didn't chair lot publicise. Racially materials mind speakers still but shivers its screaming its.

Under number. Articles content our big very act subconscious about avoid common paper costs. Below reason another are your and ten chris. Education conditions set told why derivative impersonating back materials costs usually the. Put will ip few far unlawful fifteen last these contributors dog. Brave play slide nature suffer racial safety returning them value spiders. So trademark adapt world original 1998. Translate offence while removed severe true materials next. Removed she removal minutes there screaming case unacceptable is over comes distribute. Raising prevail. Already still article sounds offence returning took removal what was children aren't. Perhaps don't suspended name secondary. Minutes worldwide sublicenseable lead. Again impersonating kids once scream loud. Just details comes materials suggested now.
"""


colours_regex = "red|green|blue|yellow|orange|pink|brown|white|black"

# The findall returns a list containing all the matches. Each match is a string.
matches = re.findall(colours_regex,random_text)
print("The following colours where found:")
for match in matches:
    print("\t" + match)