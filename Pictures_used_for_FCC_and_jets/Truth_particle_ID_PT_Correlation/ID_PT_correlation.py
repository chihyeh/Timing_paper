#========Data-MC comparison for Electron=====#
import ROOT
import os
import math
from ROOT import TFile, TH1F, gDirectory, TCanvas, TPad, TProfile,TGraph, TGraphAsymmErrors,TGraphErrors
from ROOT import TH1D, TH1, TH1I
from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle
from ROOT import TLegend
from ROOT import TMath
from ROOT import TPaveText
from ROOT import TLatex
from array import array

f1= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev40mm_pythia6_zprime40tev_ww_with_Eta_cut_for_component_check_truth.root",'r')

h1 = f1.Get("h_Particles_Rank_T_vs_PT0")

c = TCanvas("c1", "c1",0,0,500,500)
gStyle.SetOptStat(0)

leg = TLegend(0.5,0.1,0.7,0.3)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextSize(0.04)
leg.SetBorderSize(0)
leg.SetTextFont(22)
leg.Draw()
h1.GetXaxis().SetRangeUser(0,7)
h1.GetYaxis().SetRangeUser(-2,5)
h1.SetXTitle("Particle ID")
h1.SetYTitle("Log(PT)")
h1.SetZTitle("Arbitrary number")


'''
if(variable[var]=="shower_depth_out"):
h3 = TH1F("h3","Ratio histogram",40,5,15)
h3=h1.Clone("h3")
h3.Divide(h2)
h1.SetTitle("Shower Depth Data/MC comparison")
h2.SetTitle("Shower Depth Data/MC comparison")
h1.SetXTitle("SHDepth(X0)")
h2.SetXTitle("SHDepth(X0)")
h1.SetYTitle("Event number")
h2.SetYTitle("Event number")
leg.AddEntry(h1,str(Found_energy[found_energy])+"GeV_Ele_data","lep")
leg.AddEntry(h2,str(Found_energy[found_energy])+"GeV_Ele_MC","l")
leg.Draw()
if(variable[var]=="shower_depth_in"):
h3 = TH1F("h3","Ratio histogram",40,5,15)
h3=h1.Clone("h3")
h3.Divide(h2)
h1.SetTitle("Shower Depth Data/MC comparison")
h2.SetTitle("Shower Depth Data/MC comparison")
h1.SetXTitle("SHDepth(X0)")
h2.SetXTitle("SHDepth(X0)")
h1.SetYTitle("Event number")
h2.SetYTitle("Event number")
leg.AddEntry(h1,str(Found_energy[found_energy])+"GeV_Ele_data","lep")
leg.AddEntry(h2,str(Found_energy[found_energy])+"GeV_Ele_MC","l")
leg.Draw()

if(variable[var]=="total_energy"):
h1.SetTitle("Total Energy Data/MC comparison")
h2.SetTitle("Total Energy Data/MC comparison")
h1.SetXTitle("MIP")
h2.SetXTitle("MIP")
h1.SetYTitle("Event number")
h2.SetYTitle("Event number")
leg.AddEntry(h1,str(Found_energy[found_energy])+"GeV_Ele_data","lep")
leg.AddEntry(h2,str(Found_energy[found_energy])+"GeV_Ele_MC","l")

if(variable[var]=="total_energy_last_three_layer"):
h3 = TH1F("h3","Ratio histogram",300,0,300)
h3=h1.Clone("h3")
h3.Divide(h2)
h1.SetTitle("Last Three Layer Energy Data/MC comparison")
h2.SetTitle("Last Three Layer Energy Data/MC comparison")
h1.SetXTitle("MIP")
h2.SetXTitle("MIP")
h1.SetYTitle("Event number")
h2.SetYTitle("Event number")
leg.AddEntry(h1,str(Found_energy[found_energy])+"GeV_Ele_data","lep")
leg.AddEntry(h2,str(Found_energy[found_energy])+"GeV_Ele_MC","l")
leg.Draw()
'''

h1.GetYaxis().SetLabelSize(0.03)
h1.GetXaxis().SetTitleFont(22)
h1.GetYaxis().SetTitleFont(22)
h1.GetXaxis().SetLabelFont(22)
h1.GetYaxis().SetLabelFont(22)

h1.Draw("colz")

c.Print("ID_PT_Correlation_WW_40TeV.pdf")







