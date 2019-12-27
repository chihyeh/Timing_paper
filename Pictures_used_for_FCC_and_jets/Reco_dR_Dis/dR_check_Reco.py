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
list_PT_T = ["T","PT"]
energy=["5","10","20","40"]
for E in range(4):
    f1= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev"+str(energy[E])+"mm_pythia6_zprime"+str(energy[E])+"tev_qq_with_Eta_cut_for_component_check_1_reco.root",'r')
    f2= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev"+str(energy[E])+"mm_pythia6_zprime"+str(energy[E])+"tev_ww_with_Eta_cut_for_component_check_1_reco.root",'r')
    

    myTree_QQ = f1.Get("BDT_variables_Reco")
    myTree_WW = f2.Get("BDT_variables_Reco")
    for j in range(2):
        for i in range(5):
            h1 = TH1F ("QQ_plot","QQ_plot",100,0,0.5)
            h2 = TH1F ("WW_plot","WW_plot",100,0,0.5)
            for iii in range(int(myTree_QQ.GetEntriesFast())):
                myTree_QQ.GetEntry(iii)
                A      = myTree_QQ.dR_Tr1T_HPt_Reco
                B      = myTree_QQ.dR_Tr1T_HPt_Reco
                C      = myTree_QQ.dR_Tr2T_HPt_Reco
                D      = myTree_QQ.dR_Tr3T_HPt_Reco
                EE     = myTree_QQ.dR_Tr4T_HPt_Reco
                G      = myTree_QQ.dR_Tr0PT_HPt_Reco
                H      = myTree_QQ.dR_Tr1PT_HPt_Reco
                I      = myTree_QQ.dR_Tr2PT_HPt_Reco
                J      = myTree_QQ.dR_Tr3PT_HPt_Reco
                K      = myTree_QQ.dR_Tr4PT_HPt_Reco
                if(j==0):
                    if(i==0):
                        h1.Fill(A)
                    if(i==1):
                        h1.Fill(B)
                    if(i==2):
                        h1.Fill(C)
                    if(i==3):
                        h1.Fill(D)
                    if(i==4):
                        h1.Fill(EE)
                if(j==1):
                    if(i==0):
                        h1.Fill(G)
                    if(i==1):
                        h1.Fill(H)
                    if(i==2):
                        h1.Fill(I)
                    if(i==3):
                        h1.Fill(J)
                    if(i==4):
                        h1.Fill(K)
            for iii in range(int(myTree_WW.GetEntriesFast())):
                myTree_WW.GetEntry(iii)
                A      = myTree_WW.dR_Tr1T_HPt_Reco
                B      = myTree_WW.dR_Tr1T_HPt_Reco
                C      = myTree_WW.dR_Tr2T_HPt_Reco
                D      = myTree_WW.dR_Tr3T_HPt_Reco
                EE     = myTree_WW.dR_Tr4T_HPt_Reco
                G      = myTree_WW.dR_Tr0PT_HPt_Reco
                H      = myTree_WW.dR_Tr1PT_HPt_Reco
                I      = myTree_WW.dR_Tr2PT_HPt_Reco
                J      = myTree_WW.dR_Tr3PT_HPt_Reco
                K      = myTree_WW.dR_Tr4PT_HPt_Reco
                if(j==0):
                    if(i==0):
                        h2.Fill(A)
                    if(i==1):
                        h2.Fill(B)
                    if(i==2):
                        h2.Fill(C)
                    if(i==3):
                        h2.Fill(D)
                    if(i==4):
                        h2.Fill(EE)
                if(j==1):
                    if(i==0):
                        h2.Fill(G)
                    if(i==1):
                        h2.Fill(H)
                    if(i==2):
                        h2.Fill(I)
                    if(i==3):
                        h2.Fill(J)
                    if(i==4):
                        h2.Fill(K)

            print 'binX: '+str(h2.GetBinContent(2))
            h1.Sumw2()
            h1.Scale(1/h1.Integral())
            h2.Sumw2()
            h2.Scale(1/h2.Integral())

            # Now you have acess to the leaves/branches of each entry in the tree, e.g.
            c = TCanvas("c1", "c1",0,0,500,500)
            gStyle.SetOptStat(0)

            leg = TLegend(0.15,0.7,0.45,0.9)
            leg.SetFillColor(0)
            leg.SetFillStyle(0)
            leg.SetTextSize(0.04)
            leg.SetBorderSize(0)
            leg.SetTextFont(22)
            leg.Draw()

            h1.SetLineColor(1)
            h1.SetLineWidth(2)
            h1.SetLineStyle(7)

            h2.SetLineColor(2)
            h2.SetLineWidth(2)
            h2.SetLineStyle(1)

            h2.GetYaxis().SetRangeUser(0,0.3)
            h2.GetXaxis().SetLimits(0,0.2)

            h2.SetTitle("#DeltaR_"+str(list_PT_T[j])+"_"+str(i))
            h2.SetTitle("#DeltaR_"+str(list_PT_T[j])+"_"+str(i))
            h2.SetXTitle("#DeltaR")
            h2.SetXTitle("#DeltaR")
            h2.SetYTitle("Arbitrary number")
            h2.SetYTitle("Arbitrary number")
            h2.SetTitle("")
            leg.AddEntry(h1,"Z'("+str(energy[E])+"TeV)#rightarrowq#bar{q}#rightarrow1 subjet","l")
            leg.AddEntry(h2,"Z'("+str(energy[E])+"TeV)#rightarrowW^{+}W^{-}#rightarrow2 subjets","l")

            leg.Draw()

            h1.GetYaxis().SetLabelSize(0.03)
            h2.GetYaxis().SetLabelSize(0.03)
            h1.GetXaxis().SetTitleFont(22)
            h2.GetXaxis().SetTitleFont(22)
            h1.GetYaxis().SetTitleFont(22)
            h2.GetYaxis().SetTitleFont(22)
            h1.GetXaxis().SetLabelFont(22)
            h2.GetXaxis().SetLabelFont(22)
            h1.GetYaxis().SetLabelFont(22)
            h2.GetYaxis().SetLabelFont(22)

            h2.Draw("hist")
            h1.Draw("histsame")

            leg.Draw()

            c.Print(str(energy[E])+"TeV_Reco/dR_"+str(list_PT_T[j])+"_"+str(i)+"_"+str(energy[E])+"TeV_Reco.pdf")





