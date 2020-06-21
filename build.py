import os

endcode = """
local efi = ""
inet.rawRequest(
    "https://raw.githubusercontent.com/KKosty4ka/Opencomputers-dualboot/master/efi.lua",
    nil,
    nil,
    function(chunk)
        efi = efi .. chunk
    end,
    8
)
component.eeprom.set(efi)
"""

ignore = ["build.py", "efi.lua", "home/.shrc", "icon.pic", "app.lua"]

filepaths = []

for d, dirs, files in os.walk(os.curdir):
	for f in files:
		filepaths.append( (d + "\\" + f)[2:].replace("\\", "/") )

filepaths = filter(lambda x: x not in ignore, filepaths)

with open("app.lua", "w") as fp:
	fp.write("local inet = require(\"Internet\")\n")

	for f in filepaths:
		fp.write("inet.download(\"https://raw.githubusercontent.com/KKosty4ka/Opencomputers-dualboot/master/" + f + "\", \"/" + f + "\")\n")

	fp.write(endcode)
	fp.close()