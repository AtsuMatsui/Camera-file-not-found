# Camera-file-not-found-fix

English / [日本語](./README_ja.md)

<p align="center">
  <img src="images/Camera_file_not_found.png" alt="required_connections" width="600">
</p>
When you open the old Nuke script, sometimes you might see this dialog showing up.  
This occurs when Nuke can't load a Camera from the original file path.
If you double-click the Camera node, Nuke may crash immediately.
To solve this issue I made a code that replaces the outdated path with a new one in Nuke.  

###

[Click here](./fix_camera_file.py)
