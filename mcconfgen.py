#Minecraft Server Properties Generator
#explanation of settings can be found at
#https://minecraft.gamepedia.com/Server.properties
print("Minecraft Server Configuration Generator")
print("begin server.properties configuration")

file1 = open("server.properties", "a")

sppr = input("Spawn-Protection Area(16):")
if sppr != "":
  file1.writelines("spawn-protection=" + sppr + "\n")
else:
  file1.writelines("spawn-protection=16" + "\n")

mati = input("Max tick time in ms(60000):")
if mati != "":
    file1.writelines("max-tick-time=" + mati + "\n")
else:
    file1.writelines("max-tick-time=60000" + "\n")

qupo = input("query.port(25565):")
if qupo != "":
    file1.writelines("query.port=" + qupo + "\n")
else:
    file1.writelines("query.port=25565" + "\n")

gese = input("Generator Settings(null):")
if gese != "":
    file1.writelines("generator-settings=" + gese + "\n")
else:
    file1.writelines("generator-settings=" + "\n")

sych = input("Sync Chunk writes(true):")
if sych != "":
    file1.writelines("sync-chunk-writes=" + sych + "\n")
else:
    file1.writelines("sync-chunk-writes=true" + "\n")

foga = input("force gamemode(false):")
if foga != "":
    file1.writelines("force-gamemode=" + foga + "\n")
else:
    file1.writelines("force-gamemode=false" + "\n")

alne = input("allow nether(true):")
if alne != "":
    file1.writelines("allow-nether=" + alne + "\n")
else:
    file1.writelines("allow-nether=true" + "\n")

enwh = input("enforce whitelist(false):")
if enwh != "":
    file1.writelines("enforce-whitelist=" + enwh + "\n")
else:
    file1.writelines("enforce-whitelist=false" + "\n")

gamo = input("gamemode(survival):")
if gamo != "":
    file1.writelines("gamemode=" + gamo + "\n")
else:
    file1.writelines("gamemode=survival" + "\n")

brco = input("broadcast console to ops(true):")
if brco != "":
    file1.writelines("broadcast-console-to-ops=" + brco + "\n")
else:
    file1.writelines("broadcast-console-to-ops=true" + "\n")

enqu = input("enable query(false):")
if enqu != "":
    file1.writelines("enable-query=" + enqu + "\n")
else:
    file1.writelines("enable-query=false" + "\n")

plid = input("player idle timeout(0):")
if plid != "":
    file1.writelines("player-idel-timeout=" + plid + "\n")
else:
    file1.writelines("player-idle-timeout=0" + "\n")

diff = input("difficulty(easy):")
if diff != "":
    file1.writelines("difficulty=" + diff + "\n")
else:
    file1.writelines("difficulty=easy" + "\n")

spmo = input("spawn monsters(true):")
if spmo != "":
    file1.writelines("spawn-monsters=" + spmo + "\n")
else:
    file1.writelines("spawn-monsters=true" + "\n")

brrc = input("broadcast rcon to ops(true):")
if spmo != "":
    file1.writelines("broadcast-rcon-to-ops=" + brrc + "\n")
else:
    file1.writelines("broadcast-rcon-to-ops=true" + "\n")

oppe = input("op permission level(4):")
if oppe != "":
    file1.writelines("op-permission-level=" + oppe + "\n")
else:
    file1.writelines("op-permission-level=4" + "\n")

pvp = input("pvp(true):")
if oppe != "":
    file1.writelines("pvp=" + pvp + "\n")
else:
    file1.writelines("pvp=true" + "\n")

enbr = input("entity broadcast range percentage(100):")
if enbr != "":
    file1.writelines("entity-broadcast-range-percentage=" + enbr + "\n")
else:
    file1.writelines("entity-broadcast-range-percentage=100" + "\n")

snen = input("snooper enabled(true):")
if snen != "":
    file1.writelines("snooper-enabled=" + snen + "\n")
else:
    file1.writelines("snooper-enabled=true" + "\n")

lety = input("level type(default):")
if lety != "":
    file1.writelines("level-type=" + lety + "\n")
else:
    file1.writelines("level-type=default" + "\n")

enst = input("enable status(true):")
if enst != "":
    file1.writelines("enable-status=" + enst + "\n")
else:
    file1.writelines("enable-status=true" + "\n")

haco = input("hardcore(false):")
if haco != "":
    file1.writelines("hardcore=" + haco + "\n")
else:
    file1.writelines("hardcore=false" + "\n")

enco = input("enable command block(true):")
if enco != "":
    file1.writelines("enable-command-block=" + enco + "\n")
else:
    file1.writelines("enable-command-block=true" + "\n")

mapl = input("max players(20):")
if mapl != "":
    file1.writelines("max-players=" + mapl + "\n")
else:
    file1.writelines("max-players=20" + "\n")

neco = input("network compression threshold(256):")
if neco != "":
    file1.writelines("network-compression-threshold=" + neco + "\n")
else:
    file1.writelines("network-compression-threshold=256" + "\n")

repash = input("resource-pack-sha1(null):")
if repash != "":
    file1.writelines("resource-pack-sha1=" + repash + "\n")
else:
    file1.writelines("resource-pack-sha1=" + "\n")

mawo = input("max-world-size(29999984):")
if mawo != "":
    file1.writelines("max-world-size=" + mawo + "\n")
else:
    file1.writelines("max-world-size=29999984" + "\n")

fupe = input("function-permission-level(2):")
if fupe != "":
    file1.writelines("function-permission-level=" + fupe + "\n")
else:
    file1.writelines("function-permission-level=2" + "\n")

rcpo = input("rcon.port(25575):")
if rcpo != "":
    file1.writelines("rcon.port=" + rcpo + "\n")
else:
    file1.writelines("rcon.port=25575" + "\n")   

sepo = input("server-port(25565):")
if sepo != "":
    file1.writelines("server-port=" + sepo + "\n")
else:
    file1.writelines("server-port=25565" + "\n")

tepa = input("texture-pack(null):")
if tepa != "":
    file1.writelines("texture-pack=" + tepa + "\n")
else:
    file1.writelines("texture-pack=" + "\n")

seip = input("server-ip(null):")
if seip != "":
    file1.writelines("server-ip=" + seip + "\n")
else:
    file1.writelines("server-ip=" + "\n")

spnp = input("spawn-npcs(true):")
if spnp != "":
    file1.writelines("spawn-npcs=" + spnp + "\n")
else:
    file1.writelines("spawn-npcs=true" + "\n")

alfl = input("allow flight(false):")
if alfl != "":
    file1.writelines("allow-flight=" + alfl + "\n")
else:
    file1.writelines("allow-flight=false" + "\n")

lena = input("level name(world):")
if lena != "":
    file1.writelines("level-name=" + lena + "\n")
else:
    file1.writelines("level-name=world" + "\n")

vidi = input("view distance(10):")
if vidi != "":
    file1.writelines("view-distance=" + vidi + "\n")
else:
    file1.writelines("view-distance=10" + "\n")

repa = input("resource pack(null):")
if repa != "":
    file1.writelines("resource-pack=" + repa + "\n")
else:
    file1.writelines("resource-pack=" + "\n")

span = input("spawn animals(true):")
if span != "":
    file1.writelines("spawn-animals=" + span + "\n")
else:
    file1.writelines("spawn-animals=true" + "\n")

whli = input("white list(false):")
if whli != "":
    file1.writelines("white-list=" + whli + "\n")
else:
    file1.writelines("white-list=false" + "\n")

rcpa = input("rcon password(holebuild):")
if rcpa != "":
    file1.writelines("rcon.password=" + rcpa + "\n")
else:
    file1.writelines("rcon.password=holebuild" + "\n")

gest = input("generate structures(true):")
if gest != "":
    file1.writelines("generate-structures=" + gest + "\n")
else:
    file1.writelines("generate-structures=true" + "\n")

onmo = input("online mode(true):")
if onmo != "":
    file1.writelines("online-mode=" + onmo + "\n")
else:
    file1.writelines("online-mode=true" + "\n")

mabu = input("max build height(256):")
if mabu != "":
    file1.writelines("max-build-height=" + mabu + "\n")
else:
    file1.writelines("max-build-height=256" + "\n")

lese = input("level seed(null):")
if lese != "":
    file1.writelines("level-seed=" + lese + "\n")
else:
    file1.writelines("level-seed=" + "\n")

usna = input("use native transport(true):")
if usna != "":
    file1.writelines("use-native-transport=" + usna + "\n")
else:
    file1.writelines("use-native-transport=true" + "\n")

prpr = input("prevent proxy connections(false):")
if prpr != "":
    file1.writelines("prevent-proxy-connections=" + prpr + "\n")
else:
    file1.writelines("prevent-proxy-connections=false" + "\n")

enjmx = input("enable jmx monitoring(false):")
if enjmx != "":
    file1.writelines("enable-jmx-monitoring=" + enjmx + "\n")
else:
    file1.writelines("enable-jmx-monitoring=false" + "\n")

motd = input("motd(A Vanilla Minecraft Server):")
if motd != "":
    file1.writelines("motd=" + motd + "\n")
else:
    file1.writelines("motd=A Vanilla Minecraft Server" + "\n")

enrc = input("enable rcon(true):")
if enrc != "":
    file1.writelines("enable-rcon=" + enrc + "\n")
else:
    file1.writelines("enable-rcon=true" + "\n")

file1.close()
