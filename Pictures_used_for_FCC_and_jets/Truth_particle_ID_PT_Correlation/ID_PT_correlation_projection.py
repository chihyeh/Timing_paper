#========Data-MC comparison for Electron=====#
import ROOT
import os
import math
from ROOT import TFile, TH1F, gDirectory, TCanvas, TPad, TProfile,TGraph, TGraphAsymmErrors,TGraphErrors
from ROOT import TH1D, TH1, TH1I, TCut, TCutG
from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle
from ROOT import TLegend
from ROOT import TMath
from ROOT import TPaveText
from ROOT import TLatex
from array import array
import numpy as np

for Sort_particle in range(1,8):
    f1= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev5mm_pythia6_zprime5tev_qq_with_Eta_cut_for_component_check_truth.root",'r')
    h1 = f1.Get("h_Particles_Rank_T_vs_PT0")
    f2= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev5mm_pythia6_zprime5tev_ww_with_Eta_cut_for_component_check_truth.root",'r')
    h2 = f2.Get("h_Particles_Rank_T_vs_PT0")


    c = TCanvas("c1", "c1",0,0,500,500)
    gStyle.SetOptStat(0)

    '''
    cutg1 = TCutG("cutg1",5)
    cutg1.SetPoint(0,0,0)
    cutg1.SetPoint(1,8,0)
    cutg1.SetPoint(2,8,3)
    cutg1.SetPoint(3,0,3)
    cutg1.SetPoint(4,0,0)
    '''
    Fraction_QQ=array("f",[])
    Fraction_WW=array("f",[])
    X_PT=array("f",[])
    X_Error=array("f",[])
    Y_Error_QQ=array("f",[])
    Y_Error_WW=array("f",[])

    overfloat_bin_content_WW=0
    overfloat_bin_content_QQ=0
    for Bin in range(1,7):
        
        X_PT.append(-1.25+0.5*Bin)
        X_Error.append(0.25)

        if(Bin>1 and Bin<6):
            H1_Projection = h1.ProjectionX("1",Bin+2,Bin+2,"")
            H2_Projection = h2.ProjectionX("2",Bin+2,Bin+2,"")
            if(H1_Projection.Integral()!=0):
                H1_Projection.Sumw2()
                H1_Projection.Scale(1/H1_Projection.Integral())
                Fraction_QQ_Use=H1_Projection.GetBinContent(Sort_particle)
                Fraction_QQ.append(Fraction_QQ_Use)
                Y_Error_QQ.append(np.sqrt(H1_Projection.GetEntries()*Fraction_QQ_Use*(1-Fraction_QQ_Use))/H1_Projection.GetEntries())
            else:
                Fraction_QQ.append(0)
                Y_Error_QQ.append(0)


            if(H2_Projection.Integral()!=0):
                H2_Projection.Sumw2()
                H2_Projection.Scale(1/H2_Projection.Integral())
                Fraction_WW_Use=H2_Projection.GetBinContent(Sort_particle)
                Fraction_WW.append(Fraction_WW_Use)
                Y_Error_WW.append(np.sqrt(H2_Projection.GetEntries()*Fraction_WW_Use*(1-Fraction_WW_Use))/H2_Projection.GetEntries())
            else:
                Y_Error_WW.append(0)
                Fraction_WW.append(0)
                   
        if(Bin==1 or Bin==6):
            if(Bin==1):
                H1_Projection = h1.ProjectionX("1",Bin,Bin+1,"")
                H2_Projection = h2.ProjectionX("2",Bin,Bin+1,"")
            if(Bin==6):
                H1_Projection = h1.ProjectionX("1",Bin+2,Bin+4,"")
                H2_Projection = h2.ProjectionX("2",Bin+2,Bin+4,"")

            if(H1_Projection.Integral()!=0):
                H1_Projection.Sumw2()
                H1_Projection.Scale(1/H1_Projection.Integral())
                Fraction_QQ_Use=H1_Projection.GetBinContent(Sort_particle)
                Fraction_QQ.append(Fraction_QQ_Use)
                Y_Error_QQ.append(np.sqrt(H1_Projection.GetEntries()*Fraction_QQ_Use*(1-Fraction_QQ_Use))/H1_Projection.GetEntries())
            #print 'H1_Projection.GetBinContent(5): '+str(H1_Projection.GetBinContent(Sort_particle))
            else:
                Fraction_QQ.append(0)
                Y_Error_QQ.append(0)
            #   print 'H1_Projection.GetBinContent(5): '+str(0)
    
    
            if(H2_Projection.Integral()!=0):
                H2_Projection.Sumw2()
                H2_Projection.Scale(1/H2_Projection.Integral())
                Fraction_WW_Use=H2_Projection.GetBinContent(Sort_particle)
                Fraction_WW.append(Fraction_WW_Use)
                Y_Error_WW.append(np.sqrt(H2_Projection.GetEntries()*Fraction_WW_Use*(1-Fraction_WW_Use))/H2_Projection.GetEntries())
            else:
                Fraction_QQ.append(0)
                Y_Error_QQ.append(0)


    gr_QQ = TGraphErrors(6,X_PT,Fraction_QQ,X_Error,Y_Error_QQ)
    gr_QQ.SetLineColor(1)
    gr_QQ.SetLineWidth(1)
    gr_QQ.SetLineStyle(1)
    gr_QQ.SetMarkerColor(1)
    gr_QQ.SetMarkerStyle(8)
    gr_QQ.SetMarkerSize(1)
    gr_QQ.GetXaxis().SetTitle("Log(PT)")
    gr_QQ.GetYaxis().SetTitle("Arbitrary")

    gr_WW = TGraphErrors(6,X_PT,Fraction_WW,X_Error,Y_Error_WW)
    gr_WW.SetLineColor(3)
    gr_WW.SetLineWidth(1)
    gr_WW.SetLineStyle(1)
    gr_WW.SetMarkerColor(2)
    gr_WW.SetMarkerStyle(8)
    gr_WW.SetMarkerSize(1)
    #gr.GetXaxis().SetTitle("E[TeV]")
    #gr.GetXaxis().SetTitleColor(4)
    #gr.GetYaxis().SetTitle("<T_{delay>}")

    #gr_QQ.SetTitle("<T_{delay}>[ns] Vs E[TeV]")
    gr_QQ.Draw("ALP")
    gr_WW.Draw("LPsame")

    gr_QQ.GetHistogram().SetMaximum(1.2)
    gr_QQ.GetHistogram().SetMinimum(0)
    gr_QQ.GetXaxis().SetLimits(-1,2)
    gr_QQ.GetXaxis().CenterTitle()
    gr_QQ.GetYaxis().CenterTitle()

    #=================================
    leg1=TLegend(0.15,0.75,0.35,0.9)
    leg1.SetFillColor(0)
    leg1.SetFillStyle(0)
    leg1.SetTextSize(0.04)
    leg1.SetBorderSize(0)
    leg1.SetTextFont(22)
    leg1.AddEntry(gr_QQ,"Z'(5TeV)#rightarrowq#bar{q}#rightarrow1 subjet","lp")
    leg1.AddEntry(gr_WW,"Z'(5TeV)#rightarrowW^{+}W^{-}#rightarrow2 subjets","lp")

    c.Draw()
    leg1.Draw()
    c.Print(str(Sort_particle)+"_Fraction.pdf")






