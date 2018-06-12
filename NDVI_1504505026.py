# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from osgeo import gdal
from osgeo import ogr
from osgeo.gdal import GetDriverByName
from pyproj import Proj
import numpy
from numpy import nan_to_num
import os
from gdalconst import *
from PIL import Image
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm



###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 820,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Landsat B4" ), wx.VERTICAL )
		
		self.m_gb4 = wx.StaticBitmap( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
		sbSizer8.Add( self.m_gb4, 0, wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer8.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_openb4 = wx.FilePickerCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a metadatafile", u"*.*", wx.DefaultPosition, wx.Size( 250,-1 ), wx.FLP_DEFAULT_STYLE )
		sbSizer8.Add( self.m_openb4, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Landsat B5" ), wx.VERTICAL )
		
		self.m_gb5 = wx.StaticBitmap( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
		sbSizer9.Add( self.m_gb5, 0, wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer9.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_openb5 = wx.FilePickerCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a metadatafile", u"*.*", wx.DefaultPosition, wx.Size( 250,-1 ), wx.FLP_DEFAULT_STYLE )
		sbSizer9.Add( self.m_openb5, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NDVI" ), wx.VERTICAL )
		
		self.m_gndvi = wx.StaticBitmap( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
		sbSizer11.Add( self.m_gndvi, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer11.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_save = wx.Button( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Simpan NDVI", wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		sbSizer11.Add( self.m_save, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( sbSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Input Metadata" ), wx.VERTICAL )
		
		self.m_metadata = wx.FilePickerCtrl( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a metadatafile", u"*.*", wx.DefaultPosition, wx.Size( 800,-1 ), wx.FLP_DEFAULT_STYLE )
		sbSizer14.Add( self.m_metadata, 0, wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel6 = wx.Panel( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( sbSizer14.GetStaticBox(), wx.ID_ANY, u"Koordinat" ), wx.VERTICAL )
		
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Awal Lat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer7.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_ul_lat = wx.TextCtrl( sbSizer16.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 189,-1 ), 0 )
		fgSizer7.Add( self.m_ul_lat, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Awal Lon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer7.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_ul_lon = wx.TextCtrl( sbSizer16.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 189,-1 ), 0 )
		fgSizer7.Add( self.m_ul_lon, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Akhir Lat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer7.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_lr_lat = wx.TextCtrl( sbSizer16.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 189,-1 ), 0 )
		fgSizer7.Add( self.m_lr_lat, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Akhir Lon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer7.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_lr_lon = wx.TextCtrl( sbSizer16.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 189,-1 ), 0 )
		fgSizer7.Add( self.m_lr_lon, 0, wx.ALL, 5 )
		
		
		sbSizer16.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		self.m_proses = wx.Button( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Proses", wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		sbSizer16.Add( self.m_proses, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( sbSizer16, 1, wx.EXPAND, 5 )
		
		self.m_panel5 = wx.Panel( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		sbSizer14.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( sbSizer14, 1, wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		self.m_loading = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 800,-1 ), wx.GA_HORIZONTAL )
		self.m_loading.SetValue( 0 ) 
		bSizer9.Add( self.m_loading, 0, wx.ALL, 5 )
		
		
		fgSizer4.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_openb4.Bind( wx.EVT_FILEPICKER_CHANGED, self.B4_Open )
		self.m_openb5.Bind( wx.EVT_FILEPICKER_CHANGED, self.B5_Open )
		self.m_save.Bind( wx.EVT_BUTTON, self.Save_metadatafile )
		self.m_metadata.Bind( wx.EVT_FILEPICKER_CHANGED, self.Get_metadata )
		self.m_proses.Bind( wx.EVT_BUTTON, self.Proses_citra )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def B4_Open(self, event):
		try:
			alamatb4 = self.m_openb4.GetPath()
			self.bacab4 = gdal.Open(alamatb4, GA_ReadOnly)
			gambarb4 = wx.Bitmap(alamatb4, wx.BITMAP_TYPE_TIF)
			gambar = wx.Bitmap.ConvertToImage(gambarb4)
			skala = gambar.Scale(250, 250, wx.IMAGE_QUALITY_HIGH)
			hasil = wx.BitmapFromImage(skala)
			self.m_gb4.SetBitmap(hasil)
		except Exception as e:
			print(e)
			pass
		event.Skip()

	def B5_Open(self, event):
		try:
			alamatb5 = self.m_openb5.GetPath()
			self.bacab5 = gdal.Open(alamatb5, GA_ReadOnly)
			gambarb5 = wx.Bitmap(alamatb5, wx.BITMAP_TYPE_TIF)
			gambar = wx.Bitmap.ConvertToImage(gambarb5)
			skala = gambar.Scale(250, 250, wx.IMAGE_QUALITY_HIGH)
			hasil = wx.BitmapFromImage(skala)
			self.m_gb5.SetBitmap(hasil)
		except Exception as e:
			print(e)
			pass
		event.Skip()

	def Save_metadatafile(self, event):
		dialogEksplor = wx.FileDialog(frame, 'Save to TIF', '', '', 'GeoTiff Files(*.tif)|*.tif',
									   wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

		if dialogEksplor.ShowModal() == wx.ID_OK:
			alamat = dialogEksplor.GetPath()
			self.saveFile(alamat)
			self.Message("Info", "File Telah Disimpan!")
		else:
			self.Message("Info", "Terjadi Kesalahan! Gagal menyimpan data")
		event.Skip()

	def Message(self, title, desc):
		dialog = wx.MessageDialog(None, desc, title, wx.OK | wx.ICON_INFORMATION)
		dialog.ShowModal()
		event.Skip()

	def saveFile(self, dir):
		ekstensi = gdal.GetDriverByName('GTiff')
		gambar_array = self.hasil.astype(numpy.float32)
		keluaran = ekstensi.Create(dir, self.keluaran_kolom, self.keluaran_baris, 1, gdal.GDT_Float32)
		keluaran_band = keluaran.GetRasterBand(1)
		keluaran_band.SetNoDataValue(-99)
		keluaran_band.WriteArray(gambar_array)
		keluaran.SetGeoTransform(self.bacab4.GetGeoTransform())

	def Get_metadata(self, event):
		alamat = self.m_metadata.GetPath()
		self.metadata = self.readMetadata(alamat)
		self.m_ul_lat.SetValue(str(self.metadata['CORNER_UL_LAT_PRODUCT']))
		self.m_ul_lon.SetValue(str(self.metadata['CORNER_UL_LON_PRODUCT']))
		self.m_lr_lat.SetValue(str(self.metadata['CORNER_LR_LAT_PRODUCT']))
		self.m_lr_lon.SetValue(str(self.metadata['CORNER_LR_LON_PRODUCT']))
		event.Skip()

	def readMetadata(self, Meta):
		metadatafile = open(Meta, 'r')
		keluaran = {}
		for line in metadatafile.readlines():
			if "=" in line:
				l = line.split("=")
				keluaran[l[0].strip()] = l[1].strip()

		if not len(keluaran) > 0:
			keluaran = None

		return keluaran

	def Proses_citra(self, event):
		B4 = self.m_openb4.GetPath()
		B5 = self.m_openb5.GetPath()
		self.m_loading.SetRange(100)
		lon_awal = self.m_ul_lon.GetValue()
		lat_awal = self.m_ul_lat.GetValue()
		lon_akhir = self.m_lr_lon.GetValue()
		lat_akhir = self.m_lr_lat.GetValue()
		self.Crop_data(B4, B5, lon_awal, lat_awal, lon_akhir, lat_akhir)

	# Crop data
	def Crop_data(self, B4, B5, lon_awal, lat_awal, lon_akhir, lat_akhir):
		bandb4 = gdal.Open(B4)
		bandb5 = gdal.Open(B5)
		
		# Menhitung kolom, baris, bandb4
		kolom = bandb4.RasterXSize
		baris = bandb4.RasterYSize
		banbandb4 = bandb4.RasterCount
		self.m_loading.SetValue(5)
		
		# Fungsi matrix
		matriksb4 = bandb4.GetGeoTransform()
		self.matriksb4 = matriksb4
		x0 = matriksb4[0]
		y0 = matriksb4[3]
		pwidth = matriksb4[1]
		pheight = matriksb4[5]
		x_end = kolom * pwidth + x0
		y_end = baris * pheight + y0
		self.m_loading.SetValue(20)
		
		#deklarasikan longitude dan latitude
		myProj = Proj('+proj=utm +zone=50, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs')
		lon, lat = myProj(matriksb4[0], matriksb4[3], inverse=True)
		x_utm, y_utm = myProj(lon, lat)

		lon_mulai_crop = lon_awal
		lat_mulai_crop = lat_awal
		lon_akhir_crop = lon_akhir
		lat_akhir_crop = lat_akhir

		x_mulai_crop_utm, y_mulai_crop_utm = myProj(lon_mulai_crop, lat_mulai_crop)
		x_akhir_crop_utm, y_akhir_crop_utm = myProj(lon_akhir_crop, lat_akhir_crop)
		self.m_loading.SetValue(22)
		
		# 2. Cari Index Array
		xoff = int((x_mulai_crop_utm - x0) / pwidth)  # menentukan array awal pemotongan
		yoff = int((y_mulai_crop_utm - y0) / pheight)  # menentukan array akhir pemotongan
		self.m_loading.SetValue(25)
		self.keluaran_kolom = int((x_akhir_crop_utm - x_mulai_crop_utm) / pwidth)
		self.keluaran_baris = int((y_akhir_crop_utm - y_mulai_crop_utm) / pheight)

		band_B4 = bandb4.GetRasterBand(1)
		band_B5 = bandb5.GetRasterBand(1)

		#proses ndvi
		dataB4 = band_B4.ReadAsArray(xoff, yoff, 2000, 2000).astype(numpy.uint32)
		dataB5 = band_B5.ReadAsArray(xoff, yoff, 2000, 2000).astype(numpy.uint32)
		self.array_b4 = dataB4
		self.array_b5 = dataB5
		self.m_loading.SetValue(30)

		data_B4 = band_B4.ReadAsArray(xoff, yoff, self.keluaran_kolom, self.keluaran_baris)
		data_B5 = band_B5.ReadAsArray(xoff, yoff, self.keluaran_kolom, self.keluaran_baris)
		self.m_loading.SetValue(50)

		print("\nData Band 4: \n", data_B4, "\n")
		print("Data Band 5: \n", data_B5, "\n")

		data_B4_32 = data_B4.astype(numpy.float32)
		data_B5_32 = data_B5.astype(numpy.float32)
		
		#rumus ndvi = (Nir - Red)/(Nir+red)
		ndvi = ((data_B5_32-data_B4_32)/(data_B5_32+data_B4_32))
		self.m_loading.SetValue(60)

		self.hasil = ndvi

		#tampil ndvi
		rgb = ndvi * 255

		#convert arrayndvi menjadi citra rgb
		gambarndvi = Image.fromarray(rgb).convert('RGB')
		gambar = wx.EmptyImage(gambarndvi.size[0], gambarndvi.size[1])
		gambar.SetData(gambarndvi.tobytes())
		self.m_loading.SetValue(80)

		#pemotongan citra sesuai panel
		H = gambar.GetHeight()
		W = gambar.GetWidth()
		if W > H:
			NewW = 250
			NewH = 250 * H / W
		else:
			NewH = 250
			NewW = 250 * W / H
		gambar = gambar.Scale(NewW, NewH)
		self.m_gndvi.SetBitmap(wx.Bitmap(gambar))
		self.m_loading.SetValue(100)


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = MyFrame2(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
	

