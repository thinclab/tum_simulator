#!/usr/bin/env python 

import roslib; roslib.load_manifest('cvg_sim_gazebo')
import rospy
rospy.init_node('gen_dae')

import sys
import string

dae_string = '''
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<COLLADA xmlns="http://www.collada.org/2005/11/COLLADASchema" version="1.4.1">
    <asset>
        <contributor>
            <authoring_tool>SketchUp 8.0.16846</authoring_tool>
        </contributor>
        <created>2013-02-14T18:43:01Z</created>
        <modified>2013-02-14T18:43:01Z</modified>
        <up_axis>Z_UP</up_axis>
    </asset>
    <library_visual_scenes>
        <visual_scene id="ID1">
            <node name="SketchUp">
                <instance_geometry url="#ID2">
                    <bind_material>
                        <technique_common>
                            <instance_material symbol="Material2" target="#ID4">
                                <bind_vertex_input semantic="UVSET0" input_semantic="TEXCOORD" input_set="0" />
                            </instance_material>
                        </technique_common>
                    </bind_material>
                </instance_geometry>
                <instance_geometry url="#ID10">
                    <bind_material>
                        <technique_common>
                            <instance_material symbol="Material2" target="#ID11">
                                <bind_vertex_input semantic="UVSET0" input_semantic="TEXCOORD" input_set="0" />
                            </instance_material>
                        </technique_common>
                    </bind_material>
                </instance_geometry>
            </node>
        </visual_scene>
    </library_visual_scenes>
    <library_geometries>
        <geometry id="ID2">
            <mesh>
                <source id="ID5">
                    <float_array id="ID8" count="60">
                        {w} {h} 0
                        0 0 0
                        0 {h} 0
                        {w} 0 0
                        0 {h} 0.001
                        {w} {h} 0
                        0 {h} 0
                        {w} {h} 0.001
                        {w} {h} 0
                        {w} 0 0.001
                        {w} 0 0
                        {w} {h} 0.001
                        {w} 0 0.001
                        0 0 0
                        {w} 0 0
                        0 0 0.001
                        0 {h} 0.001
                        0 0 0
                        0 0 0.001
                        0 {w} 0
                    </float_array>
                    <technique_common>
                        <accessor count="20" source="#ID8" stride="3">
                            <param name="X" type="float" />
                            <param name="Y" type="float" />
                            <param name="Z" type="float" />
                        </accessor>
                    </technique_common>
                </source>
                <source id="ID6">
                    <float_array id="ID9" count="60">0 0 -1 0 0 -1 0 0 -1 0 0 -1 -0 1 0 -0 1 0 -0 1 0 -0 1 0 1 0 0 1 0 0 1 0 0 1 0 0 -0 -1 -0 -0 -1 -0 -0 -1 -0 -0 -1 -0 -1 0 0 -1 0 0 -1 0 0 -1 0 0</float_array>
                    <technique_common>
                        <accessor count="20" source="#ID9" stride="3">
                            <param name="X" type="float" />
                            <param name="Y" type="float" />
                            <param name="Z" type="float" />
                        </accessor>
                    </technique_common>
                </source>
                <vertices id="ID7">
                    <input semantic="POSITION" source="#ID5" />
                    <input semantic="NORMAL" source="#ID6" />
                </vertices>
                <triangles count="10" material="Material2">
                    <input offset="0" semantic="VERTEX" source="#ID7" />
                    <p>0 1 2 1 0 3 4 5 6 5 4 7 8 9 10 9 8 11 12 13 14 13 12 15 16 17 18 17 16 19</p>
                </triangles>
            </mesh>
        </geometry>
        <geometry id="ID10">
            <mesh>
                <source id="ID16">
                    <float_array id="ID20" count="12">
                        {w} 0 0.001 
                        0 {h} 0.001
                        0 0 0.001
                        {w} {h} 0.001
                    </float_array>
                    <technique_common>
                        <accessor count="4" source="#ID20" stride="3">
                            <param name="X" type="float" />
                            <param name="Y" type="float" />
                            <param name="Z" type="float" />
                        </accessor>
                    </technique_common>
                </source>
                <source id="ID17">
                    <float_array id="ID21" count="12">-0 -0 1 -0 -0 1 -0 -0 1 -0 -0 1</float_array>
                    <technique_common>
                        <accessor count="4" source="#ID21" stride="3">
                            <param name="X" type="float" />
                            <param name="Y" type="float" />
                            <param name="Z" type="float" />
                        </accessor>
                    </technique_common>
                </source>
                <source id="ID19">
                    <float_array id="ID22" count="8">1 0 0 1 0 0 1 1</float_array>
                    <technique_common>
                        <accessor count="4" source="#ID22" stride="2">
                            <param name="S" type="float" />
                            <param name="T" type="float" />
                        </accessor>
                    </technique_common>
                </source>
                <vertices id="ID18">
                    <input semantic="POSITION" source="#ID16" />
                    <input semantic="NORMAL" source="#ID17" />
                </vertices>
                <triangles count="2" material="Material2">
                    <input offset="0" semantic="VERTEX" source="#ID18" />
                    <input offset="1" semantic="TEXCOORD" source="#ID19" />
                    <p>0 0 1 1 2 2 1 1 0 0 3 3</p>
                </triangles>
            </mesh>
        </geometry>
    </library_geometries>
    <library_materials>
        <material id="ID4" name="material">
            <instance_effect url="#ID3" />
        </material>
        <material id="ID11" name="material_1">
            <instance_effect url="#ID12" />
        </material>
    </library_materials>
    <library_effects>
        <effect id="ID3">
            <profile_COMMON>
                <technique sid="COMMON">
                    <lambert>
                        <diffuse>
                            <color>1 1 1 1</color>
                        </diffuse>
                    </lambert>
                </technique>
            </profile_COMMON>
        </effect>
        <effect id="ID12">
            <profile_COMMON>
                <newparam sid="ID14">
                    <surface type="2D">
                        <init_from>ID13</init_from>
                    </surface>
                </newparam>
                <newparam sid="ID15">
                    <sampler2D>
                        <source>ID14</source>
                    </sampler2D>
                </newparam>
                <technique sid="COMMON">
                    <lambert>
                        <diffuse>
                            <texture texture="ID15" texcoord="UVSET0" />
                        </diffuse>
                    </lambert>
                </technique>
            </profile_COMMON>
        </effect>
    </library_effects>
    <library_images>
        <image id="ID13">
            <init_from>/grid.png</init_from>
        </image>
    </library_images>
    <scene>
        <instance_visual_scene url="#ID1" />
    </scene>
</COLLADA>
'''.format(h=string.atof(sys.argv[1])*string.atof(sys.argv[3]), w=string.atof(sys.argv[2])*string.atof(sys.argv[4]))

dae_file = open(sys.argv[5], "w")
dae_file.write(dae_string)
dae_file.close()
