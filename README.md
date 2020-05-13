# MinecraftPython
Run commands in Python and build Images!

## Before Running
Before you can use this program, you will need to install the following package: `pillow`

## Running you first program!
To run your first program, you need to get the path to your world (press Win+R, type %AppData% and open your .minecraft folder. Then go to saves and get the path to your save.
Now download the folder and create a new python file in the same directory of the downloaded folder.

To start, you need to type following:

```
import minecraft

cmd = minecraft.cmd(WorldPath, datapackName)
```

You can choose your own datapack name!

If you done this your first time with this world, you will need to leave and join it again.

## Say something in chat
After you steps above you can now type something in Chat:

```
cmd.sayInChat("Hi. This was a Test!")
```

## Run your own command
To run a command, write

```
cmd.run(command)
```

in chat. Dont use "/" in the beginning of the command (e. g. `say hi`)

## Print images in your world

To build a image you will need to define some variables:

```
ImagePath : Path to your Image
PositionToPlace: Position where to place the image
BlockTypes: Which blocks can be used (e. g. `BlockTypes = [cmd.types.wool, cmd.types.concrete]`, or if you want all blocks: `BlockTypes = [cmd.types.all]`
TexturePath: Set Path to unzipped texturepack. Without a Texturepack the programm wouldnt know which Block has which color.
ImageScale: The Scale of the image.
Axis: In which direction to place the image.
Fast: Say if you want to run it in one tick (only for smaller images) or if the image can load row after row. Default: False (row after row)
```

After you made this variables, you can type:

```
cmd.build_image(ImagePath, PositionToPlace, BlockTypes, TexturePath, ImageScale, Axis, Fast)
```

## Examples
There are two examples in the downloadfile named `example.py` and `help.py`
