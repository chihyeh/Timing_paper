#========Data-MC comparison for Electron=====#
import ROOT
import os
import math
from ROOT import TFile, TH1F, gDirectory, TCanvas, TPad, TProfile,TGraph, TGraphAsymmErrors,TGraphErrors,TText
from ROOT import TH1D, TH1, TH1I
from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle
from ROOT import TLegend
from ROOT import TMath
from ROOT import TPaveText
from ROOT import TLatex
from array import array

list_PT_T = ["T","PT"]
energy = ["5","10","20","40"]
for E in range(1):
    for j in range(2):
        for i in range(5):
            f1= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev"+str(energy[E])+"mm_pythia6_zprime"+str(energy[E])+"tev_qq_with_Eta_cut_for_component_check_truth.root",'r')
            f2= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev"+str(energy[E])+"mm_pythia6_zprime"+str(energy[E])+"tev_ww_with_Eta_cut_for_component_check_truth.root",'r')
            f3= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev5mm_pythia6_zprime5tev_qq_with_Eta_cut_for_component_check_1.root",'r')
            f4= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev5mm_pythia6_zprime5tev_ww_with_Eta_cut_for_component_check_1.root",'r')

            h1 = f1.Get("h_Particles_Rank_"+str(list_PT_T[j])+"_"+str(i))
            h2 = f2.Get("h_Particles_Rank_"+str(list_PT_T[j])+"_"+str(i))
            h3 = f3.Get("Total_particle_ID_eta_cut")
            h4 = f4.Get("Total_particle_ID_eta_cut")
            h5 = f3.Get("Total_particle_ID_eta_PT_cut")
            h6 = f4.Get("Total_particle_ID_eta_PT_cut")

            h1.Sumw2()
            h1.Scale(1/h1.Integral())
            h2.Sumw2()
            h2.Scale(1/h2.Integral())
            h3.Sumw2()
            h3.Scale(1/h3.Integral())
            h4.Sumw2()
            h4.Scale(1/h4.Integral())
            h5.Sumw2()
            h5.Scale(1/h5.Integral())
            h6.Sumw2()
            h6.Scale(1/h6.Integral())


            a = TH1F ("a","a",5,0,50)
            a.Fill(-1)

            c = TCanvas("c1", "c1",0,0,500,500)
            gStyle.SetOptStat(0)

            leg = TLegend(0.15,0.75,0.35,0.9)
            leg.SetFillColor(0)
            leg.SetFillStyle(0)
            leg.SetTextSize(0.04)
            leg.SetBorderSize(0)
            leg.SetTextFont(22)
            leg.Draw()

            h1.SetLineColor(1)
            h1.SetLineWidth(2)
            h1.SetLineStyle(1)

            h2.SetLineColor(2)
            h2.SetLineWidth(2)
            h2.SetLineStyle(10)

            h3.SetLineColor(3)
            h3.SetLineWidth(1)
            h3.SetLineStyle(1)

            h4.SetLineColor(4)
            h4.SetLineWidth(2)
            h4.SetLineStyle(1)

            h5.SetLineColor(7)
            h5.SetLineWidth(2)
            h5.SetLineStyle(1)

            h6.SetLineColor(6)
            h6.SetLineWidth(2)
            h6.SetLineStyle(1)


            h1.SetMarkerStyle(9)
            h2.SetMarkerStyle(9)
            h3.SetMarkerStyle(9)
            h4.SetMarkerStyle(9)
            h5.SetMarkerStyle(9)

            h1.GetXaxis().SetRangeUser(0,8)
            h1.GetYaxis().SetRangeUser(0,1)
            h1.GetYaxis().SetRangeUser(0,1)


            t1 =  TLatex(0.3,.1,"e^{-}");
            t2 =  TLatex(1.3,.1,"#mu^{-}");
            t3 =  TLatex(2.1,.1,"K_{L}^{0}");
            t4 =  TLatex(3.1,.1,"K_{S}^{0}");
            t5 =  TLatex(4.3,.1,"#pi^{+}");
            t6 =  TLatex(5.1,.1,"K^{+}");
            t7 =  TLatex(6.3,.1,"n");
            t8 =  TLatex(7.3,.1,"p");


#h1.SetTitle("Trailing Particle ID(5TeV)"+str(list_PT_T[j])+"_"+str(i))
#            h1.SetTitle("Trailing Particle ID(5TeV)"+str(list_PT_T[j])+"_"+str(i))
            h1.SetXTitle("Kinds of particles")
            h1.SetXTitle("Kinds of particles")
            h1.SetYTitle("Arbitrary number")
            h1.SetYTitle("Arbitrary number")
            h1.SetTitle("")
            leg.AddEntry(h1,"Z'("+str(energy[E])+"TeV)#rightarrowq#bar{q}#rightarrow1 subjet","l")
            leg.AddEntry(h2,"Z'("+str(energy[E])+"TeV)#rightarrowW^{+}W^{-}#rightarrow2 subjets","l")

            leg.Draw()

            #Z'("+str(energy_array[1][m])+"TeV)#rightarrowt#bar{t}#rightarrow3 jet
            #Z'("+str(energy_array[1][m])+"TeV)#rightarrowq#bar{q}#rightarrow1 jet
            #Z'("+str(energy_array[1][m])+"TeV)#rightarrowW^{+}W^{-}#rightarrow2 jet
            h3.GetYaxis().SetLabelSize(0.03)
            h4.GetYaxis().SetLabelSize(0.03)
            h3.GetXaxis().SetTitleFont(22)
            h4.GetXaxis().SetTitleFont(22)
            h3.GetYaxis().SetTitleFont(22)
            h4.GetYaxis().SetTitleFont(22)
            h3.GetXaxis().SetLabelFont(22)
            h4.GetXaxis().SetLabelFont(22)
            h3.GetYaxis().SetLabelFont(22)
            h4.GetYaxis().SetLabelFont(22)

            h1.Draw("hist")
            h2.Draw("histsame")

            #h3.Draw("hist")
            #h4.Draw("histsame")
            #h5.Draw("histsame")
            #h6.Draw("histsame")

            t1.Draw("same")
            t2.Draw("same")
            t3.Draw("same")
            t4.Draw("same")
            t5.Draw("same")
            t6.Draw("same")
            t7.Draw("same")
            t8.Draw("same")

            leg.Draw()

            c.Print(str(energy[E])+"TeV/h_"+str(energy[E])+"TeV_Particles_Rank_"+str(list_PT_T[j])+"_"+str(i)+".pdf")







