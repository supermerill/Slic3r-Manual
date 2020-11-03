% Print Settings

This page will provide an overview of the available configuration settings in
Slic3r. Every configuration option has a tooltip and it is recommended to read
those tooltips. 

Print Settings
--------------

The `Print Settings` tab provides the opportunity to change settings
related to the actual print. Whereas the other tabs are changed rarely,
the settings on this tab will be modified regularly, possibly for each
model printed.

![Print Settings: Layers and Perimeters](images/print_settings_1.png "fig:")


#### Vertical Shells

`Perimeters` defines the minimum number of vertical shells (i.e. walls)
a print will have. Unless the model requires single width walls it is
generally recommended to have a minimum of two perimeters as this gives
some insurance that if a section of the perimeter is not printed
correctly then the second perimeter will help cover it. For structural parts 4 perimeters may be required.

`Spiral Vase` is for producing decorative (but weak objects). There is only a single layer, with the nozzle continuously creeping upwards like a corkscrew.


#### Horizontal Shells
`Solid Layers` is quite simply the number of layers the slicer will stack on top of each other at the top or bottom of the model. Never go below 2 layers unless for test purposes as the top will not be strong. If you are using variable layer height, it is worth setting `Minimum shell thickness` too.

`Minimum shell thickness` defines the top and bottom solid thickness in millimetres instead of layers. This is useful if you are using variable layer height but want to keep a defined physical thickness. Note that if this thickness is greater than the equivalent layers set in `Solid Layers` it will override `Solid Layers`.

`Enforce 100% fill volume` is an experimental option. Refer to the in-slicer tooltip for information as this feature is subject to change.


#### Quality
`Only one perimeter on top surfaces` overrides the normal `Perimeters` setting and limits it to a single perimeter. This provides more space to the infill pattern (and ironing too if enabled).

`Minimum width` **need to add explanatory images with this to aid description**

`Extra perimeters on overhangs` can be useful on severe overhangs. The slicer will keep adding additional perimeters until there is no visible gap. This will override the standard `Perimeters` setting.

`Extra perimeters on odd layers` **need to add explanatory images with this to aid description**

`Ensure vertical shell thickness` **need to document the difference between this and the extra perimeters on overhangs**

`Avoid crossing perimeters` Will alter the planning of travel moves to minimise crossing perimeters. Useful if you have ooze issues from the extruder. Note that it does not guarantee zero perimeter crossings.

`Avoid crossing perimeters not on first layer` **why separate the first layer?**

`Overlapping external perimeter` **need to add explanatory images with this to aid description**

`Overlapping external perimeter also for all perimeters` **need to add explanatory images with this to aid description**

`Thin walls` Enable this to allow the slicer to detect walls less than two extrusions thick. If unchecked the slicer may try to fit two perimeters, leading to over extrusion.

`Thin walls min width` This sets the threshold where the slicer will create a thin wall vs. when it will choose to simply extrude a thicker perimeter.

`Thin walls overlap` **need to add explanatory images with this to aid description**

`Thin walls merging with perimeters` **need to add explanatory images with this to aid description**

#### Overhangs

`Threshold for bridge speed and fan` defines what width of extrusion (as % or mm) must be unsupported for the slicer to consider it a bridge. Bridge speed and fan values are then applied (this does not apply bridge flow).

`Threshold for bridge flow` defines what width of extrusion (as % or mm) must be unsupported for the slicer to consider it a bridge. Bridge flow is then applied (this does not apply bridge speed or fan values).

`Extrusion direction reverse on odd` Each perimeter which is is in an overhang alternates direction on each layer. So the first layer may be extruded clockwise, the second anticlockwise, then clockwise, etc. This provides most benefit on steep overhangs. **Add photos here with and without this setting enabled**

`Extrusion direction reverse threshold` **need to understand what this setting does**


#### Advanced





