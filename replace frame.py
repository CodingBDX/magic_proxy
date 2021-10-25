
ZeroBin.net is a minimalist, open source online pastebin where the server has zero knowledge of pasted data. Data is encrypted/decrypted in the browser using 256 bits AES. More information on the project page.
www.Zerobin.net is not affiliated with the ZeroBin project or the PrivateBin project.

Click here to visit the public Guest Book.

By using this site you agree to the Terms Of Service.

ZeroBin.net
Because ignorance is bliss
Find us on Tor Onionspace:
http://zerobinqmdqd236y.onion
Onion V3:
http://zerobinftagjpeeebbvyzjcqyjpmjvynj5qlexwyxe7l3vqejxnqv5qd.onion

# Version 1.1
# By DrainLife#3361
#
# Known issues
# Does not support double faced card backs (mdfc, etc)


function Rename-Card {
	Param(
		# What you want to refer to the frame as in the finished image. ie: Card Name (Template Name).png
		# Use Call with NONE to simply have Card Name.png
		[Parameter(Mandatory, Position = 0)][string]$Template,
		# Option to send to Frames folder instead of completed cards
		[Parameter()][switch]$Frame
	)
	
	$srcpath = ".\images\fronts\" # Path to Proximtiy Output Images with trailing \
	if ($Frame) {
		$dstpath = ".\Completed\Frames\" # Path to folder for completed frames with trailing \
	} else {
		$dstpath = ".\Completed\" # Path to folder for completed proxies with trailing \
	}
	
	
	# Create Directory if it does not exist.
	if (!(Test-Path -PathType Container $dstpath)) {
		Write-Host "Path did not exist, creating..."
		New-Item -ItemType Directory -Force -Path $dstpath
	}
	

	$srclist = Get-ChildItem -Path $srcpath

	foreach ($srcimage in $srclist) {
		if ($Template -eq "NONE") {
			$dstimage = $srcimage.name -replace "^\d+ (.*).png","`$1.png"
		}
		else {
			$dstimage = $srcimage.name -replace "^\d+ (.*).png","`$1 ($Template).png"
		}
		$srcimage = $srcpath + $srcimage.name
		$dstimage = $dstpath + $dstimage
		Move-Item "$srcimage" "$dstimage" -Force
	}
}

### Complete Cards

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=chillis-0.4.0
Rename-Card "NONE"

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=normalExtended
Rename-Card "Extended"

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=blackextended
Rename-Card "Extended Black"

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=pinlinesExtended
Rename-Card "Extended Pinlines"

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=DnD
Rename-Card "DnD"

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=pinlinesExtendedNeon
Rename-Card "Extended Pinlines Neon"

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=InventionBlueSilver --copyright=false
Rename-Card "InventionBlueSilver"

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=InventionBronze --copyright=false
Rename-Card "InventionBronze"

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=InventionSilver --copyright=false
Rename-Card "InventionSilver"

java -jar proximity.jar --cards=deck.txt --use_official_art=true --reminder_text=true --template=mystical
Rename-Card "Mystical"

#### Frames Only for finishing with PS/GIMP

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=chillis-0.4.0
Rename-Card "NONE" -Frame

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=normalExtended
Rename-Card "Extended" -Frame

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=blackextended
Rename-Card "Extended Black" -Frame

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=pinlinesExtended
Rename-Card "Extended Pinlines" -Frame

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=DnD
Rename-Card "DnD" -Frame

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=pinlinesExtendedNeon
Rename-Card "Extended Pinlines Neon" -Frame

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=InventionBlueSilver --copyright=false
Rename-Card "InventionBlueSilver" -Frame

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=InventionBronze --copyright=false
Rename-Card "InventionBronze" -Frame

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=InventionSilver --copyright=false
Rename-Card "InventionSilver" -Frame

java -jar proximity.jar --cards=deck.txt --reminder_text=true --template=mystical
Rename-Card "Mystical" -Frame


