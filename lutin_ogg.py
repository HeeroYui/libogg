#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import lutin.debug as debug

def get_desc():
	return "ogg : Ogg-tremor library for ogg audio decoding"


def create(target):
	myModule = module.Module(__file__, 'ogg', 'LIBRARY')
	
	myModule.add_src_file([
		'ogg/framing.c',
		'ogg/bitwise.c',
		'tremor/floor0.c',
		'tremor/vorbisfile.c',
		'tremor/synthesis.c',
		'tremor/res012.c',
		'tremor/block.c',
		'tremor/mdct.c',
		'tremor/sharedbook.c',
		'tremor/codebook.c',
		'tremor/floor1.c',
		'tremor/window.c',
		'tremor/registry.c',
		'tremor/info.c',
		'tremor/mapping0.c'
		])
	myModule.compile_version_CC(1989, gnu=True)
	myModule.compile_flags('c', "-Wno-duplicate-decl-specifier")
	if target.name=="Android":
		myModule.compile_flags('c', "-DBYTE_ORDER=1")
		myModule.compile_flags('c', "-DBIG_ENDIAN=0")
		myModule.compile_flags('c', "-DLITTLE_ENDIAN=1")
	
	myModule.add_export_path(tools.get_current_path(__file__))
	myModule.add_path(tools.get_current_path(__file__)+"/ogg/")
	myModule.add_path(tools.get_current_path(__file__)+"/tremor/")
	
	# add the currrent module at the 
	return myModule









