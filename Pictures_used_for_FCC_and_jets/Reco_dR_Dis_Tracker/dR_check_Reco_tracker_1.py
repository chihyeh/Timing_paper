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
list_PT_T = ["PT"]
energy=["5","10","20","40"]
for E in range(4):
    f1= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev"+str(energy[E])+"mm_pythia6_zprime"+str(energy[E])+"tev_qq_with_Eta_cut_for_component_check_1_reco_Com.root",'r')
    f2= ROOT.TFile.Open("/Users/ms08962476/singularity/TIming_Studies/tev"+str(energy[E])+"mm_pythia6_zprime"+str(energy[E])+"tev_ww_with_Eta_cut_for_component_check_1_reco_Com.root",'r')
    

    myTree_QQ = f1.Get("BDT_variables_Reco_track")
    myTree_WW = f2.Get("BDT_variables_Reco_track")
    for j in range(1):
        h1  = TH1F ("QQ_plot0","QQ_plot0",20,0,0.1)
        h2  = TH1F ("WW_plot0","WW_plot0",20,0,0.1)
        h3  = TH1F ("QQ_plot1","QQ_plot1",20,0,0.1)
        h4  = TH1F ("WW_plot1","WW_plot1",20,0,0.1)
        h5  = TH1F ("QQ_plot2","QQ_plot2",20,0,0.1)
        h6  = TH1F ("WW_plot2","WW_plot2",20,0,0.1)
        h7  = TH1F ("QQ_plot3","QQ_plot3",20,0,0.1)
        h8  = TH1F ("WW_plot3","WW_plot3",20,0,0.1)
        h9  = TH1F ("QQ_plot4","QQ_plot4",20,0,0.1)
        h10 = TH1F ("WW_plot4","WW_plot4",20,0,0.1)

        for iii in range(int(myTree_QQ.GetEntriesFast())):
            myTree_QQ.GetEntry(iii)
            A      = myTree_QQ.dR_Tr0T_HPt_Reco_track
            B      = myTree_QQ.dR_Tr1T_HPt_Reco_track
            C      = myTree_QQ.dR_Tr2T_HPt_Reco_track
            D      = myTree_QQ.dR_Tr3T_HPt_Reco_track
            EE     = myTree_QQ.dR_Tr4T_HPt_Reco_track
            G      = myTree_QQ.dR_Tr0PT_HPt_Reco_track
            H      = myTree_QQ.dR_Tr1PT_HPt_Reco_track
            I      = myTree_QQ.dR_Tr2PT_HPt_Reco_track
            J      = myTree_QQ.dR_Tr3PT_HPt_Reco_track
            K      = myTree_QQ.dR_Tr4PT_HPt_Reco_track
            if(j==0):
                if(A < 0.1):
                    h1.Fill(A)
                else:
                    h1.Fill(0.099999)
                if(B < 0.1):
                    h3.Fill(B)
                else:
                    h3.Fill(0.099999)
                if(C < 0.1):
                    h5.Fill(C)
                else:
                    h5.Fill(0.099999)
                if(D < 0.1):
                    h7.Fill(D)
                else:
                    h7.Fill(0.099999)
                if(EE < 0.1):
                    h9.Fill(EE)
                else:
                    h9.Fill(0.099999)
            if(j==1):
                if(G < 0.1):
                    h1.Fill(G)
                else:
                    h1.Fill(0.099999)
                if(H < 0.1):
                    h3.Fill(H)
                else:
                    h3.Fill(0.099999)
                if(I < 0.1):
                    h5.Fill(I)
                else:
                    h5.Fill(0.099999)
                if(J < 0.1):
                    h7.Fill(J)
                else:
                    h7.Fill(0.099999)
                if(K < 0.1):
                    h9.Fill(K)
                else:
                    h9.Fill(0.099999)
        for iii in range(int(myTree_WW.GetEntriesFast())):
            myTree_WW.GetEntry(iii)
            A      = myTree_WW.dR_Tr0T_HPt_Reco_track
            B      = myTree_WW.dR_Tr1T_HPt_Reco_track
            C      = myTree_WW.dR_Tr2T_HPt_Reco_track
            D      = myTree_WW.dR_Tr3T_HPt_Reco_track
            EE     = myTree_WW.dR_Tr4T_HPt_Reco_track
            G      = myTree_WW.dR_Tr0PT_HPt_Reco_track
            H      = myTree_WW.dR_Tr1PT_HPt_Reco_track
            I      = myTree_WW.dR_Tr2PT_HPt_Reco_track
            J      = myTree_WW.dR_Tr3PT_HPt_Reco_track
            K      = myTree_WW.dR_Tr4PT_HPt_Reco_track
            if(j==0):
                if(A < 0.1):
                    h2.Fill(A)
                else:
                    h2.Fill(0.099999)
                if(B < 0.1):
                    h4.Fill(B)
                else:
                    h4.Fill(0.099999)
                if(C < 0.1):
                    h6.Fill(C)
                else:
                    h6.Fill(0.099999)
                if(D < 0.1):
                    h8.Fill(D)
                else:
                    h8.Fill(0.099999)
                if(EE < 0.1):
                    h10.Fill(EE)
                else:
                    h10.Fill(0.099999)
            if(j==1):
                if(G < 0.1):
                    h2.Fill(G)
                else:
                    h2.Fill(0.099999)
                if(H < 0.1):
                    h4.Fill(H)
                else:
                    h4.Fill(0.099999)
                if(I < 0.1):
                    h6.Fill(I)
                else:
                    h6.Fill(0.099999)
                if(J < 0.1):
                    h8.Fill(J)
                else:
                    h8.Fill(0.099999)
                if(K < 0.1):
                    h10.Fill(K)
                else:
                    h10.Fill(0.099999)

        print 'binX: '+str(h2.GetBinContent(2))
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
        h7.Sumw2()
        h7.Scale(1/h7.Integral())
        h8.Sumw2()
        h8.Scale(1/h8.Integral())
        h9.Sumw2()
        h9.Scale(1/h9.Integral())
        h10.Sumw2()
        h10.Scale(1/h10.Integral())

        # Now you have acess to the leaves/branches of each entry in the tree, e.g.
        c = TCanvas("c1", "c1",0,0,500,500)
        gStyle.SetOptStat(0)

        h1.SetLineColor(1)
        h1.SetLineWidth(2)
        h1.SetLineStyle(7)

        h2.SetLineColor(1)
        h2.SetLineWidth(2)
        h2.SetLineStyle(1)

        h3.SetLineColor(2)
        h3.SetLineWidth(2)
        h3.SetLineStyle(7)
        
        h4.SetLineColor(2)
        h4.SetLineWidth(2)
        h4.SetLineStyle(1)

        h5.SetLineColor(3)
        h5.SetLineWidth(2)
        h5.SetLineStyle(7)
        
        h6.SetLineColor(3)
        h6.SetLineWidth(2)
        h6.SetLineStyle(1)

        h7.SetLineColor(4)
        h7.SetLineWidth(2)
        h7.SetLineStyle(7)
        
        h8.SetLineColor(4)
        h8.SetLineWidth(2)
        h8.SetLineStyle(1)

        h9.SetLineColor(6)
        h9.SetLineWidth(2)
        h9.SetLineStyle(7)
        
        h10.SetLineColor(6)
        h10.SetLineWidth(2)
        h10.SetLineStyle(1)


        if(E>0):
            h2.GetYaxis().SetRangeUser(0,0.7)
            h2.GetXaxis().SetLimits(0,0.1)
        else:
            h2.GetYaxis().SetRangeUser(0,0.7)
            h2.GetXaxis().SetLimits(0,0.1)
        h2.SetTitle("#DeltaR_"+str(list_PT_T[j]))
        h2.SetTitle("#DeltaR_"+str(list_PT_T[j]))
        h2.SetXTitle("#DeltaR")
        h2.SetXTitle("#DeltaR")
        h2.SetYTitle("Arbitrary number")
        h2.SetYTitle("Arbitrary number")
        h2.SetTitle("")
#       leg.AddEntry(h1,"Z'("+str(energy[E])+"TeV)#rightarrowq#bar{q}#rightarrow1 subjet","l")
#       leg.AddEntry(h2,"Z'("+str(energy[E])+"TeV)#rightarrowW^{+}W^{-}#rightarrow2 subjets","l")

        leg = TLegend(0.25,0.5,0.45,0.9)
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.04)
        leg.SetBorderSize(0)
        leg.SetTextFont(22)
        leg.Draw()
        leg.AddEntry("","Z'#rightarrowq#bar{q}","")
        leg.AddEntry(h1,"Trailing^{1}","l")
        leg.AddEntry(h3,"Trailing^{2}","l")
        leg.AddEntry(h5,"Trailing^{3}","l")
        leg.AddEntry(h7,"Trailing^{4}","l")
        leg.AddEntry(h9,"Trailing^{5}","l")

        leg1 = TLegend(0.55,0.5,0.85,0.9)
        leg1.SetFillColor(0)
        leg1.SetFillStyle(0)
        leg1.SetTextSize(0.04)
        leg1.SetBorderSize(0)
        leg1.SetTextFont(22)
        leg1.Draw("same")
        leg1.AddEntry("","Z'#rightarrowW^{+}W^{-}","")
        leg1.AddEntry(h2,"Trailing^{1}","l")
        leg1.AddEntry(h4,"Trailing^{2}","l")
        leg1.AddEntry(h6,"Trailing^{3}","l")
        leg1.AddEntry(h8,"Trailing^{4}","l")
        leg1.AddEntry(h10,"Trailing^{5}","l")

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
        h3.Draw("histsame")
        h4.Draw("histsame")
        h5.Draw("histsame")
        h6.Draw("histsame")
        h7.Draw("histsame")
        h8.Draw("histsame")
        h9.Draw("histsame")
        h10.Draw("histsame")

        leg.Draw()
        leg1.Draw("same")

        c.Print(str(energy[E])+"TeV_Reco_track/dR_"+str(list_PT_T[j])+"_"+str(energy[E])+"TeV_Reco_track.pdf")





