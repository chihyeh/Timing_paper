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

for Sort_particle in range(8):
    f1= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev5mm_pythia6_zprime5tev_qq_with_Eta_cut_for_component_check_truth.root",'r')
    h1 = f1.Get("h_Particles_Rank_T_vs_PT0")
    f2= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev5mm_pythia6_zprime5tev_ww_with_Eta_cut_for_component_check_truth.root",'r')
    h2 = f2.Get("h_Particles_Rank_T_vs_PT0")
    f3= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev10mm_pythia6_zprime10tev_qq_with_Eta_cut_for_component_check_truth.root",'r')
    h3 = f3.Get("h_Particles_Rank_T_vs_PT0")
    f4= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev10mm_pythia6_zprime10tev_ww_with_Eta_cut_for_component_check_truth.root",'r')
    h4 = f4.Get("h_Particles_Rank_T_vs_PT0")
    f5= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev20mm_pythia6_zprime20tev_qq_with_Eta_cut_for_component_check_truth.root",'r')
    h5 = f5.Get("h_Particles_Rank_T_vs_PT0")
    f6= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev20mm_pythia6_zprime20tev_ww_with_Eta_cut_for_component_check_truth.root",'r')
    h6 = f6.Get("h_Particles_Rank_T_vs_PT0")
    f7= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev40mm_pythia6_zprime40tev_qq_with_Eta_cut_for_component_check_truth.root",'r')
    h7 = f7.Get("h_Particles_Rank_T_vs_PT0")
    f8= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev40mm_pythia6_zprime40tev_ww_with_Eta_cut_for_component_check_truth.root",'r')
    h8 = f8.Get("h_Particles_Rank_T_vs_PT0")


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
    Fraction_QQ_5TeV=array("f",[])
    Fraction_WW_5TeV=array("f",[])
    Fraction_QQ_10TeV=array("f",[])
    Fraction_WW_10TeV=array("f",[])
    Fraction_QQ_20TeV=array("f",[])
    Fraction_WW_20TeV=array("f",[])
    Fraction_QQ_40TeV=array("f",[])
    Fraction_WW_40TeV=array("f",[])

    Y_Error_QQ_5TeV=array("f",[])
    Y_Error_WW_5TeV=array("f",[])
    Y_Error_QQ_10TeV=array("f",[])
    Y_Error_WW_10TeV=array("f",[])
    Y_Error_QQ_20TeV=array("f",[])
    Y_Error_WW_20TeV=array("f",[])
    Y_Error_QQ_40TeV=array("f",[])
    Y_Error_WW_40TeV=array("f",[])

    X_PT=array("f",[])
    X_Error=array("f",[])

    overfloat_bin_content_WW=0
    overfloat_bin_content_QQ=0
    for Bin in range(1,5):
        
        X_PT.append(-0.25+0.5*Bin)
        X_Error.append(0.25)
        
        global H1_Projection_5TeV
        global H2_Projection_5TeV
        global H3_Projection_10TeV
        global H4_Projection_10TeV
        global H5_Projection_20TeV
        global H6_Projection_20TeV
        global H7_Projection_40TeV
        global H8_Projection_40TeV
        
        if(Bin>1 and Bin<4):
            H1_Projection_5TeV =  h1.ProjectionX("1",Bin+4,Bin+4,"")
            H2_Projection_5TeV =  h2.ProjectionX("2",Bin+4,Bin+4,"")
            H3_Projection_10TeV = h3.ProjectionX("3",Bin+4,Bin+4,"")
            H4_Projection_10TeV = h4.ProjectionX("4",Bin+4,Bin+4,"")
            H5_Projection_20TeV = h5.ProjectionX("5",Bin+4,Bin+4,"")
            H6_Projection_20TeV = h6.ProjectionX("6",Bin+4,Bin+4,"")
            H7_Projection_40TeV = h7.ProjectionX("7",Bin+4,Bin+4,"")
            H8_Projection_40TeV = h8.ProjectionX("8",Bin+4,Bin+4,"")
        if(Bin==1):
            H1_Projection_5TeV =  h1.ProjectionX("1",Bin,Bin+4,"")
            H2_Projection_5TeV =  h2.ProjectionX("2",Bin,Bin+4,"")
            H3_Projection_10TeV = h3.ProjectionX("3",Bin,Bin+4,"")
            H4_Projection_10TeV = h4.ProjectionX("4",Bin,Bin+4,"")
            H5_Projection_20TeV = h5.ProjectionX("5",Bin,Bin+4,"")
            H6_Projection_20TeV = h6.ProjectionX("6",Bin,Bin+4,"")
            H7_Projection_40TeV = h7.ProjectionX("7",Bin,Bin+4,"")
            H8_Projection_40TeV = h8.ProjectionX("8",Bin,Bin+4,"")
        if(Bin==4):
            H1_Projection_5TeV =  h1.ProjectionX("1",Bin+4,Bin+6,"")
            H2_Projection_5TeV =  h2.ProjectionX("2",Bin+4,Bin+6,"")
            H3_Projection_10TeV = h3.ProjectionX("3",Bin+4,Bin+12,"")
            H4_Projection_10TeV = h4.ProjectionX("4",Bin+4,Bin+12,"")
            H5_Projection_20TeV = h5.ProjectionX("5",Bin+4,Bin+12,"")
            H6_Projection_20TeV = h6.ProjectionX("6",Bin+4,Bin+12,"")
            H7_Projection_40TeV = h7.ProjectionX("7",Bin+4,Bin+12,"")
            H8_Projection_40TeV = h8.ProjectionX("8",Bin+4,Bin+12,"")
            #====================
        if(H1_Projection_5TeV.Integral()!=0):
            H1_Projection_5TeV.Sumw2()
            H1_Projection_5TeV.Scale(1/H1_Projection_5TeV.Integral())
            Fraction_QQ_Use=H1_Projection_5TeV.GetBinContent(Sort_particle)
            Fraction_QQ_5TeV.append(Fraction_QQ_Use)
            Y_Error_QQ_5TeV.append(np.sqrt(H1_Projection_5TeV.GetEntries()*Fraction_QQ_Use*(1-Fraction_QQ_Use))/H1_Projection_5TeV.GetEntries())
        else:
            Fraction_QQ_5TeV.append(0)
            Y_Error_QQ_5TeV.append(0)


        if(H2_Projection_5TeV.Integral()!=0):
            H2_Projection_5TeV.Sumw2()
            H2_Projection_5TeV.Scale(1/H2_Projection_5TeV.Integral())
            Fraction_WW_Use=H2_Projection_5TeV.GetBinContent(Sort_particle)
            Fraction_WW_5TeV.append(Fraction_WW_Use)
            Y_Error_WW_5TeV.append(np.sqrt(H2_Projection_5TeV.GetEntries()*Fraction_WW_Use*(1-Fraction_WW_Use))/H2_Projection_5TeV.GetEntries())
        else:
            Y_Error_WW_5TeV.append(0)
            Fraction_WW_5TeV.append(0)
               
        if(H3_Projection_10TeV.Integral()!=0):
            H3_Projection_10TeV.Sumw2()
            H3_Projection_10TeV.Scale(1/H3_Projection_10TeV.Integral())
            Fraction_QQ_Use=H3_Projection_10TeV.GetBinContent(Sort_particle)
            Fraction_QQ_10TeV.append(Fraction_QQ_Use)
            Y_Error_QQ_10TeV.append(np.sqrt(H3_Projection_10TeV.GetEntries()*Fraction_QQ_Use*(1-Fraction_QQ_Use))/H3_Projection_10TeV.GetEntries())
        else:
            Fraction_QQ_10TeV.append(0)
            Y_Error_QQ_10TeV.append(0)


        if(H4_Projection_10TeV.Integral()!=0):
            H4_Projection_10TeV.Sumw2()
            H4_Projection_10TeV.Scale(1/H4_Projection_10TeV.Integral())
            Fraction_WW_Use=H4_Projection_10TeV.GetBinContent(Sort_particle)
            Fraction_WW_10TeV.append(Fraction_WW_Use)
            Y_Error_WW_10TeV.append(np.sqrt(H4_Projection_10TeV.GetEntries()*Fraction_WW_Use*(1-Fraction_WW_Use))/H4_Projection_10TeV.GetEntries())
        else:
            Y_Error_WW_10TeV.append(0)
            Fraction_WW_10TeV.append(0)

        if(H5_Projection_20TeV.Integral()!=0):
            H5_Projection_20TeV.Sumw2()
            H5_Projection_20TeV.Scale(1/H5_Projection_20TeV.Integral())
            Fraction_QQ_Use=H5_Projection_20TeV.GetBinContent(Sort_particle)
            Fraction_QQ_20TeV.append(Fraction_QQ_Use)
            Y_Error_QQ_20TeV.append(np.sqrt(H5_Projection_20TeV.GetEntries()*Fraction_QQ_Use*(1-Fraction_QQ_Use))/H5_Projection_20TeV.GetEntries())
        else:
            Fraction_QQ_20TeV.append(0)
            Y_Error_QQ_20TeV.append(0)


        if(H6_Projection_20TeV.Integral()!=0):
            H6_Projection_20TeV.Sumw2()
            H6_Projection_20TeV.Scale(1/H6_Projection_20TeV.Integral())
            Fraction_WW_Use=H6_Projection_20TeV.GetBinContent(Sort_particle)
            Fraction_WW_20TeV.append(Fraction_WW_Use)
            Y_Error_WW_20TeV.append(np.sqrt(H6_Projection_20TeV.GetEntries()*Fraction_WW_Use*(1-Fraction_WW_Use))/H6_Projection_20TeV.GetEntries())
        else:
            Y_Error_WW_20TeV.append(0)
            Fraction_WW_20TeV.append(0)

        if(H7_Projection_40TeV.Integral()!=0):
            H7_Projection_40TeV.Sumw2()
            H7_Projection_40TeV.Scale(1/H7_Projection_40TeV.Integral())
            Fraction_QQ_Use=H7_Projection_40TeV.GetBinContent(Sort_particle)
            Fraction_QQ_40TeV.append(Fraction_QQ_Use)
            Y_Error_QQ_40TeV.append(np.sqrt(H7_Projection_40TeV.GetEntries()*Fraction_QQ_Use*(1-Fraction_QQ_Use))/H7_Projection_40TeV.GetEntries())
        else:
            Fraction_QQ_40TeV.append(0)
            Y_Error_QQ_40TeV.append(0)


        if(H8_Projection_40TeV.Integral()!=0):
            H8_Projection_40TeV.Sumw2()
            H8_Projection_40TeV.Scale(1/H8_Projection_40TeV.Integral())
            Fraction_WW_Use=H8_Projection_40TeV.GetBinContent(Sort_particle)
            Fraction_WW_40TeV.append(Fraction_WW_Use)
            Y_Error_WW_40TeV.append(np.sqrt(H8_Projection_40TeV.GetEntries()*Fraction_WW_Use*(1-Fraction_WW_Use))/H8_Projection_40TeV.GetEntries())
        else:
            Y_Error_WW_40TeV.append(0)
            Fraction_WW_40TeV.append(0)


    gr_QQ_5TeV = TGraphErrors(4,X_PT,Fraction_QQ_5TeV,X_Error,Y_Error_QQ_5TeV)
    gr_QQ_5TeV.SetLineColor(1)
    gr_QQ_5TeV.SetLineWidth(1)
    gr_QQ_5TeV.SetLineStyle(1)
    gr_QQ_5TeV.SetMarkerColor(1)
    gr_QQ_5TeV.SetMarkerStyle(8)
    gr_QQ_5TeV.SetMarkerSize(1)
    gr_QQ_5TeV.GetXaxis().SetTitle("Log(PT)")
    gr_QQ_5TeV.GetYaxis().SetTitle("Arbitrary")

    gr_WW_5TeV = TGraphErrors(4,X_PT,Fraction_WW_5TeV,X_Error,Y_Error_WW_5TeV)
    gr_WW_5TeV.SetLineColor(2)
    gr_WW_5TeV.SetLineWidth(1)
    gr_WW_5TeV.SetLineStyle(1)
    gr_WW_5TeV.SetMarkerColor(2)
    gr_WW_5TeV.SetMarkerStyle(8)
    gr_WW_5TeV.SetMarkerSize(1)

    gr_QQ_10TeV = TGraphErrors(4,X_PT,Fraction_QQ_10TeV,X_Error,Y_Error_QQ_10TeV)
    gr_QQ_10TeV.SetLineColor(3)
    gr_QQ_10TeV.SetLineWidth(1)
    gr_QQ_10TeV.SetLineStyle(1)
    gr_QQ_10TeV.SetMarkerColor(3)
    gr_QQ_10TeV.SetMarkerStyle(8)
    gr_QQ_10TeV.SetMarkerSize(1)

    gr_WW_10TeV = TGraphErrors(4,X_PT,Fraction_WW_10TeV,X_Error,Y_Error_WW_10TeV)
    gr_WW_10TeV.SetLineColor(4)
    gr_WW_10TeV.SetLineWidth(1)
    gr_WW_10TeV.SetLineStyle(1)
    gr_WW_10TeV.SetMarkerColor(4)
    gr_WW_10TeV.SetMarkerStyle(8)
    gr_WW_10TeV.SetMarkerSize(1)

    gr_QQ_20TeV = TGraphErrors(4,X_PT,Fraction_QQ_20TeV,X_Error,Y_Error_QQ_20TeV)
    gr_QQ_20TeV.SetLineColor(5)
    gr_QQ_20TeV.SetLineWidth(1)
    gr_QQ_20TeV.SetLineStyle(1)
    gr_QQ_20TeV.SetMarkerColor(5)
    gr_QQ_20TeV.SetMarkerStyle(8)
    gr_QQ_20TeV.SetMarkerSize(1)

    gr_WW_20TeV = TGraphErrors(4,X_PT,Fraction_WW_20TeV,X_Error,Y_Error_WW_20TeV)
    gr_WW_20TeV.SetLineColor(6)
    gr_WW_20TeV.SetLineWidth(1)
    gr_WW_20TeV.SetLineStyle(1)
    gr_WW_20TeV.SetMarkerColor(6)
    gr_WW_20TeV.SetMarkerStyle(8)
    gr_WW_20TeV.SetMarkerSize(1)

    gr_QQ_40TeV = TGraphErrors(4,X_PT,Fraction_QQ_40TeV,X_Error,Y_Error_QQ_40TeV)
    gr_QQ_40TeV.SetLineColor(7)
    gr_QQ_40TeV.SetLineWidth(1)
    gr_QQ_40TeV.SetLineStyle(1)
    gr_QQ_40TeV.SetMarkerColor(7)
    gr_QQ_40TeV.SetMarkerStyle(8)
    gr_QQ_40TeV.SetMarkerSize(1)

    gr_WW_40TeV = TGraphErrors(4,X_PT,Fraction_WW_40TeV,X_Error,Y_Error_WW_40TeV)
    gr_WW_40TeV.SetLineColor(8)
    gr_WW_40TeV.SetLineWidth(1)
    gr_WW_40TeV.SetLineStyle(1)
    gr_WW_40TeV.SetMarkerColor(8)
    gr_WW_40TeV.SetMarkerStyle(8)
    gr_WW_40TeV.SetMarkerSize(1)

    #gr.GetXaxis().SetTitle("E[TeV]")
    #gr.GetXaxis().SetTitleColor(4)
    #gr.GetYaxis().SetTitle("<T_{delay>}")

    #gr_QQ.SetTitle("<T_{delay}>[ns] Vs E[TeV]")
    gr_QQ_5TeV.Draw("ALP")
    gr_WW_5TeV.Draw("LPsame")
    gr_QQ_10TeV.Draw("LPsame")
    gr_WW_10TeV.Draw("LPsame")
    gr_QQ_20TeV.Draw("LPsame")
    gr_WW_20TeV.Draw("LPsame")
    gr_QQ_40TeV.Draw("LPsame")
    gr_WW_40TeV.Draw("LPsame")

    if(Sort_particle==4):
        gr_QQ_5TeV.GetHistogram().SetMaximum(1.5)
        gr_QQ_5TeV.GetHistogram().SetMinimum(0.5)

    else:
        gr_QQ_5TeV.GetHistogram().SetMaximum(0.4)
        gr_QQ_5TeV.GetHistogram().SetMinimum(0)
    gr_QQ_5TeV.GetXaxis().SetLimits(0,2)
    gr_QQ_5TeV.GetXaxis().CenterTitle()
    gr_QQ_5TeV.GetYaxis().CenterTitle()

    #=================================
    leg1=TLegend(0.15,0.55,0.35,0.9)
    leg1.SetFillColor(0)
    leg1.SetFillStyle(0)
    leg1.SetTextSize(0.04)
    leg1.SetBorderSize(0)
    leg1.SetTextFont(22)
    leg1.AddEntry(gr_QQ_5TeV,"Z'(5TeV)#rightarrowq#bar{q}#rightarrow1 subjet","lp")
    leg1.AddEntry(gr_WW_5TeV,"Z'(5TeV)#rightarrowW^{+}W^{-}#rightarrow2 subjets","lp")
    leg1.AddEntry(gr_QQ_10TeV,"Z'(10TeV)#rightarrowq#bar{q}#rightarrow1 subjet","lp")
    leg1.AddEntry(gr_WW_10TeV,"Z'(10TeV)#rightarrowW^{+}W^{-}#rightarrow2 subjets","lp")
    leg1.AddEntry(gr_QQ_20TeV,"Z'(20TeV)#rightarrowq#bar{q}#rightarrow1 subjet","lp")
    leg1.AddEntry(gr_WW_20TeV,"Z'(20TeV)#rightarrowW^{+}W^{-}#rightarrow2 subjets","lp")
    leg1.AddEntry(gr_QQ_40TeV,"Z'(40TeV)#rightarrowq#bar{q}#rightarrow1 subjet","lp")
    leg1.AddEntry(gr_WW_40TeV,"Z'(40TeV)#rightarrowW^{+}W^{-}#rightarrow2 subjets","lp")

    c.Draw()
    leg1.Draw()
    c.Print(str(Sort_particle)+"_Fraction.pdf")






