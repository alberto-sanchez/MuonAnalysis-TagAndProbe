import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5000) ) 
# 3' for 1k vents on Run2015C, 350KB in 7' for 5k events, 2.5MB in 20' for 10k events, 90MB in 26h for 1M events on Run2015C   

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

import os
if   "CMSSW_5_3_" in os.environ['CMSSW_VERSION']:
    #process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
    process.GlobalTag.globaltag = cms.string('GR_R_53_V7::All')
    process.source.fileNames = [
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/B0C8994D-2CC7-E111-B04E-0025901D6288.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/76FB8276-3AC7-E111-A52E-001D09F297EF.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/76E299E2-2FC7-E111-B2CC-001D09F28F25.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/5C0AD4DE-4AC7-E111-9C14-001D09F23A20.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/4E4682A9-30C7-E111-9A8C-003048F1C420.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/3669603F-2FC7-E111-8935-003048D2BE06.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/0E9130E2-2FC7-E111-9494-001D09F26509.root',
        '/store/data/Run2012C/MuOnia/AOD/PromptReco-v1/000/198/208/02CA3FBC-2DC7-E111-9CA1-003048D2BB90.root',
    ]
elif "CMSSW_5_2_" in os.environ['CMSSW_VERSION']:
    #process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
    process.GlobalTag.globaltag = cms.string('GR_P_V39_AN1::All')
    process.source.fileNames = [
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/645E9BE9-FC87-E111-9D30-5404A63886C5.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/60C36C17-0188-E111-8B3D-5404A638868F.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5E384785-F087-E111-A8CB-BCAEC518FF80.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5C605E9F-F887-E111-A540-00237DDC5CB0.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5C0DCA92-CE87-E111-A539-5404A63886C6.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5A856F46-1888-E111-A3A5-BCAEC5329700.root',
        '/store/data/Run2012A/MuOnia/AOD/PromptReco-v1/000/191/226/5271187F-DF87-E111-ADDB-BCAEC518FF7C.root',
    ]
elif "CMSSW_7_4_" in os.environ['CMSSW_VERSION']:
    #from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
    #process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
    process.GlobalTag.globaltag = cms.string('GR_P_V56::All')
    process.source.fileNames = [
        # 50 ns
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/164/00000/56BA3AC3-A226-E511-98BB-02163E0133B5.root',
	#'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/167/00000/FED37D13-A826-E511-8641-02163E01386E.root',
	#'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/168/00000/1602316B-CF26-E511-BCBA-02163E011BF3.root',
        #'/store/data/Run2015B/Charmonium/AOD/PromptReco-v1/000/251/252/00000/F24C3492-9627-E511-AEC5-02163E011C7F.root'
        # 25 ns
        # redirector: root://eoscms.cern.ch/ ;   global redirector: root://cms-xrd-global.cern.ch/ ;   european redirector: root://xrootd-cms.infn.it// ;   US redirector: root://cmsxrootd.fnal.gov/ 
	#'/store/data/Run2015D/Charmonium/AOD/PromptReco-v3/000/257/822/00000/00B0174E-0869-E511-82B8-02163E01469D.root',
        #'/store/data/Run2015D/Charmonium/AOD/PromptReco-v3/000/256/629/00000/3475D421-065F-E511-9389-02163E011D45.root',
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/905/00000/1CD21CAD-BA4B-E511-A566-02163E0143A2.root',
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/905/00000/204135A9-BA4B-E511-82FE-02163E011E91.root',
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/905/00000/26E685A3-BA4B-E511-8A82-02163E012ABA.root',
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/906/00000/1CBD178C-CD4B-E511-B61D-02163E014291.root',
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/907/00000/C4A55346-E24B-E511-80E3-02163E013463.root',
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/913/00000/00716CF9-EB4B-E511-BEA7-02163E0136EE.root',
        #'/store/data/Run2015C/Charmonium/AOD/PromptReco-v1/000/254/914/00000/FCED70C1-EC4B-E511-9676-02163E0142B5.root'
	# DoubleMuon for Mu8 test
	#'root://cms-xrd-global.cern.ch//store/data/Run2015C_25ns/DoubleMuon/AOD/05Oct2015-v1/50000/001DCCA1-0574-E511-9088-0025905B85D0.root'
	# MuOnia for Mu16 test
	'/store/data/Run2015C/MuOnia/AOD/PromptReco-v1/000/254/227/00000/B4C42971-0546-E511-B988-02163E011853.root'
        ]
else: raise RuntimeError, "Unknown CMSSW version %s" % os.environ['CMSSW_VERSION']



## ==== Fast Filters ====
process.goodVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
    filter = cms.bool(True),
)
process.noScraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False), ## Or 'True' to get some per-event info
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)
process.fastFilter = cms.Sequence(process.goodVertexFilter + process.noScraping)

process.load("HLTrigger.HLTfilters.triggerResultsFilter_cfi")
process.triggerResultsFilter.triggerConditions = cms.vstring( 'HLT_Mu*_L2Mu*' )
process.triggerResultsFilter.l1tResults = ''
process.triggerResultsFilter.throw = True
process.triggerResultsFilter.hltResults = cms.InputTag( "TriggerResults", "", "HLT" )
#process.HLTMu   = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*']) # original
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*']) # original
process.HLTMu   = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*', 'HLT_Mu*_TkMu*']) # asked by Ilse
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*', 'HLT_Mu*_TkMu*']) # asked by Ilse 
process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Upsilon*', 'HLT_Mu*_TkMu*']) # my take on upsilon trigger
#process.HLTMu   = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*' ]) # for Mu8 test
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*', 'HLT_Mu*' ]) # for Mu8 test
#process.HLTBoth_withDimuon = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*', 'HLT_Mu*', 'HLT_Dimuon*' ])
process.HLTBoth_withDimuon = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Upsilon*', 'HLT_Mu*', 'HLT_Dimuon*' ]) #just in case

##    __  __                       
##   |  \/  |_   _  ___  _ __  ___ 
##   | |\/| | | | |/ _ \| '_ \/ __|
##   | |  | | |_| | (_) | | | \__ \
##   |_|  |_|\__,_|\___/|_| |_|___/
##                                 
## ==== Merge CaloMuons and Tracks into the collection of reco::Muons  ====
from RecoMuon.MuonIdentification.calomuons_cfi import calomuons;
process.mergedMuons = cms.EDProducer("CaloMuonMerger",
    mergeTracks = cms.bool(True),
    mergeCaloMuons = cms.bool(False), # AOD
    muons     = cms.InputTag("muons"), 
    caloMuons = cms.InputTag("calomuons"),
    tracks    = cms.InputTag("generalTracks"),
    minCaloCompatibility = calomuons.minCaloCompatibility,
    ## Apply some minimal pt cut
    muonsCut     = cms.string("track.isNonnull && pt > 2"),
    caloMuonsCut = cms.string("pt > 2"),
    tracksCut    = cms.string("pt > 2"),
)

## ==== Trigger matching
process.load("MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff")
## with some customization
#process.muonMatchHLTL2.maxDeltaR = 0.3 # Zoltan tuning - it was 0.5 # present in Zmumu
#process.muonMatchHLTL3.maxDeltaR = 0.1 # present in Zmumu
from MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff import *
changeRecoMuonInput(process, "mergedMuons")
#useExtendedL1Match(process) 
#addHLTL1Passthrough(process)

from MuonAnalysis.TagAndProbe.common_variables_upsilon_cff import *
process.load("MuonAnalysis.TagAndProbe.common_modules_cff")

process.tagMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string("(isGlobalMuon || numberOfMatchedStations > 1) && pt > 7.5 && !triggerObjectMatchesByCollection('hltL3MuonCandidates').empty()"),
)

process.oneTag  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tagMuons"), minNumber = cms.uint32(1))

process.probeMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    #cut = cms.string("track.isNonnull && (!triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltMuTrackJpsiCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty())"),
    cut = cms.string("track.isNonnull && !triggerObjectMatchesByCollection('hltTracksIter').empty()"),
    #cut = cms.string("") # for Mu8 test
    #cut = cms.string("track.isNonnull && !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"),
)

process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    cut = cms.string('8.6 < mass < 11.4 && abs(daughter(0).vz - daughter(1).vz) < 1'),    # mass of upsn
    decay = cms.string('tagMuons@+ probeMuons@-')
)
process.onePair = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairs"), minNumber = cms.uint32(1))

from MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cff import ExtraIsolationVariables

process.tpTree = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # choice of tag and probe pairs, and arbitration
    tagProbePairs = cms.InputTag("tpPairs"),
    arbitration   = cms.string("None"),
    # probe variables: all useful ones
    variables = cms.PSet(
        AllVariables,
        ExtraIsolationVariables,
        dxyBS = cms.InputTag("muonDxyPVdzmin","dxyBS"),
        dxyPVdzmin = cms.InputTag("muonDxyPVdzmin","dxyPVdzmin"),
        dzPV = cms.InputTag("muonDxyPVdzmin","dzPV"),
        nSplitTk  = cms.InputTag("splitTrackTagger"),
    ),
    flags = cms.PSet(
       TrackQualityFlags,
       MuonIDFlags,
       HighPtTriggerFlags,
       HighPtTriggerFlagsDebug,
       LowPtTriggerFlagsPhysics,
       LowPtTriggerFlagsEfficienciesProbe,
       Acc_JPsi = cms.string("(abs(eta) <= 1.3 && pt > 3.3) || (1.3 < abs(eta) <= 2.2 && p > 2.9) || (2.2 < abs(eta) <= 2.4  && pt > 0.8)"),
    ),
    tagVariables = cms.PSet(
        KinematicVariables, 
        nVertices = cms.InputTag("nverticesModule"),
        l1rate = cms.InputTag("l1rate"),
        bx     = cms.InputTag("l1rate","bx"),
    ),
    tagFlags = cms.PSet(
        HighPtTriggerFlags,
        HighPtTriggerFlagsDebug,
        LowPtTriggerFlagsPhysics,
        LowPtTriggerFlagsEfficienciesTag,
    ),
    pairVariables = cms.PSet(
        pt = cms.string("pt"),
        dphiVtxTimesQ = cms.InputTag("tagProbeSeparation", "dphiVtxTimesQ"),
        drM1          = cms.InputTag("tagProbeSeparation", "drM1"),
        dphiM1        = cms.InputTag("tagProbeSeparation", "dphiM1"),
        distM1        = cms.InputTag("tagProbeSeparation", "distM1"),
        drM2          = cms.InputTag("tagProbeSeparation", "drM2"),
        dphiM2        = cms.InputTag("tagProbeSeparation", "dphiM2"),
        distM2        = cms.InputTag("tagProbeSeparation", "distM2"),
        drVtx         = cms.InputTag("tagProbeSeparation", "drVtx"),
        dz            = cms.string("daughter(0).vz - daughter(1).vz"),
        probeMultiplicity = cms.InputTag("probeMultiplicity"),
    ),
    pairFlags = cms.PSet(),
    isMC           = cms.bool(False),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("probeMuons"), # was missing
)


process.load("MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cfi")

process.tnpSimpleSequence = cms.Sequence(
    process.tagMuons *
    process.oneTag     *
    process.probeMuons *
    process.tpPairs    *
    process.onePair    *
    process.muonDxyPVdzmin *
    process.nverticesModule *
    process.tagProbeSeparation *
    process.computeCorrectedIso *
    process.probeMultiplicity * 
    process.splitTrackTagger *
    process.l1rate *
    process.tpTree
)

process.tagAndProbe = cms.Path( 
    process.fastFilter *
    process.HLTBoth    *
    process.mergedMuons                 *
    process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequence
)

# OnePair tree for vertexing filter efficiency
process.tpTreeOnePair = process.tpTree.clone(
   arbitration   = "OnePair",
   # a few L1,L2,L3 variables in Ilse's file
   pairVariables = cms.PSet(
        process.tpTree.pairVariables,
        rapidity      = cms.string("rapidity"),
        absrapidity   = cms.string("abs(rapidity)"),
        #prescaled     = cms.InputTag("tagProbeSeparation", "prescaled"),
        #VtxProb       = cms.InputTag("tagProbeSeparation", "VtxProb"),
        #VtxCosPA      = cms.InputTag("tagProbeSeparation", "VtxCosPA"),
        #VtxLxy        = cms.InputTag("tagProbeSeparation", "VtxLxy"),
        #VtxLxySig     = cms.InputTag("tagProbeSeparation", "VtxLxySig"),
        #VtxL3d        = cms.InputTag("tagProbeSeparation", "VtxL3d"),
        DCA           = cms.InputTag("tagProbeSeparation", "DCA"),
        ),
)

process.tnpSimpleSequenceOnePair = cms.Sequence(
    process.tagMuons *
    process.probeMuons *
    process.tpPairs    *
    process.muonDxyPVdzmin *
    process.nverticesModule    *
    process.tagProbeSeparation *
    process.computeCorrectedIso *
    process.probeMultiplicity * 
    process.splitTrackTagger * 
    process.l1rate *
    process.tpTreeOnePair
)

process.tagAndProbeOnePair = cms.Path( 
    process.fastFilter *
    process.HLTBoth_withDimuon    *
    process.mergedMuons                 *
    process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequenceOnePair
)


##    _____               _    _             
##   |_   _| __ __ _  ___| | _(_)_ __   __ _ 
##     | || '__/ _` |/ __| |/ / | '_ \ / _` |
##     | || | | (_| | (__|   <| | | | | (_| |
##     |_||_|  \__,_|\___|_|\_\_|_| |_|\__, |
##                                     |___/ 

## Then make another collection for standalone muons, using standalone track to define the 4-momentum
process.muonsSta = cms.EDProducer("RedefineMuonP4FromTrack",
    src   = cms.InputTag("muons"),
    track = cms.string("outer"),
)
## Match to trigger, to measure the efficiency of HLT tracking
from PhysicsTools.PatAlgos.tools.helpers import *
process.patMuonsWithTriggerSequenceSta = cloneProcessingSnippet(process, process.patMuonsWithTriggerSequence, "Sta")
process.muonMatchHLTL2Sta.maxDeltaR = 0.5
process.muonMatchHLTL3Sta.maxDeltaR = 0.5
massSearchReplaceAnyInputTag(process.patMuonsWithTriggerSequenceSta, "mergedMuons", "muonsSta")

## Define probes and T&P pairs
process.probeMuonsSta = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTriggerSta"),
    cut = cms.string("outerTrack.isNonnull && !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"), 
)
process.tpPairsSta = process.tpPairs.clone(decay = "tagMuons@+ probeMuonsSta@-", cut = "5 < mass < 14")    #for upsn

process.onePairSta = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairsSta"), minNumber = cms.uint32(1))

process.staToTkMatch.maxDeltaR     = 0.3
process.staToTkMatch.maxDeltaPtRel = 2.
process.staToTkMatchNoJPsi.maxDeltaR     = 0.3
process.staToTkMatchNoJPsi.maxDeltaPtRel = 2.

process.load("MuonAnalysis.TagAndProbe.tracking_reco_info_cff")

process.tpTreeSta = process.tpTree.clone(
    tagProbePairs = "tpPairsSta",
    #arbitration   = "OneProbe", # present in Zmumu
    variables = cms.PSet(
        KinematicVariables, 
        #StaOnlyVariables, # present in Zmumu
        ## track matching variables
        tk_deltaR     = cms.InputTag("staToTkMatch","deltaR"),
        tk_deltaEta   = cms.InputTag("staToTkMatch","deltaEta"),
        tk_deltaR_NoJPsi     = cms.InputTag("staToTkMatchNoJPsi","deltaR"),
        tk_deltaEta_NoJPsi   = cms.InputTag("staToTkMatchNoJPsi","deltaEta"),
        tk_deltaR_NoBestJPsi     = cms.InputTag("staToTkMatchNoBestJPsi","deltaR"),
        tk_deltaEta_NoBestJPsi   = cms.InputTag("staToTkMatchNoBestJPsi","deltaEta"),
    ),
    flags = cms.PSet(
        #Mu5_L2Mu3_Jpsi_L2 = LowPtTriggerFlagsEfficienciesProbe.Mu5_L2Mu3_Jpsi_L2,
        LowPtTriggerFlagsPhysics,
        LowPtTriggerFlagsEfficienciesProbe,
        outerValidHits = cms.string("outerTrack.numberOfValidHits > 0"),
        TM  = cms.string("isTrackerMuon"),
        Glb = cms.string("isGlobalMuon"),
        Tk  = cms.string("track.isNonnull"),
        #StaTkSameCharge = cms.string("outerTrack.isNonnull && innerTrack.isNonnull && (outerTrack.charge == innerTrack.charge)"), # present in Zmumu
    ),
    tagVariables = cms.PSet(
        KinematicVariables, 
        nVertices = cms.InputTag("nverticesModule"),
        #combRelIso = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt"),
        #chargedHadIso04 = cms.string("pfIsolationR04().sumChargedHadronPt"),
        #neutralHadIso04 = cms.string("pfIsolationR04().sumNeutralHadronEt"),
        #photonIso04 = cms.string("pfIsolationR04().sumPhotonEt"),
        #combRelIsoPF04dBeta = IsolationVariables.combRelIsoPF04dBeta,
        #l1rate = cms.InputTag("l1rate"), # uncommented in "add bx information to data tree #18"
        #bx     = cms.InputTag("l1rate","bx"),
    ),
    tagFlags = cms.PSet(
        #Mu5_L2Mu3_Jpsi_MU = LowPtTriggerFlagsEfficienciesTag.Mu5_L2Mu3_Jpsi_MU,
        LowPtTriggerFlagsEfficienciesTag,
    ),
    pairVariables = cms.PSet(
        dz      = cms.string("daughter(0).vz - daughter(1).vz"),
        pt      = cms.string("pt"), 
        #
        dphiVtxTimesQ = cms.InputTag("tagProbeStaSeparation", "dphiVtxTimesQ"),
        drM1          = cms.InputTag("tagProbeStaSeparation", "drM1"),
        dphiM1        = cms.InputTag("tagProbeStaSeparation", "dphiM1"),
        distM1        = cms.InputTag("tagProbeStaSeparation", "distM1"),
        drM2          = cms.InputTag("tagProbeStaSeparation", "drM2"),
        dphiM2        = cms.InputTag("tagProbeStaSeparation", "dphiM2"),
        distM2        = cms.InputTag("tagProbeStaSeparation", "distM2"),
        drVtx         = cms.InputTag("tagProbeStaSeparation", "drVtx"),
        probeMultiplicity = cms.InputTag("probeStaMultiplicity"),
        #
        rapidity = cms.string("rapidity"),
        deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"), 
        ),
    pairFlags     = cms.PSet(),
    allProbes     = "probeMuonsSta", # was missing w.r.t. MC
)

process.tnpSimpleSequenceSta = cms.Sequence(
    process.tagMuons *
    process.oneTag     *
    process.probeMuonsSta *
    process.tpPairsSta      *
    process.onePairSta      *
    process.nverticesModule *
    process.tagProbeStaSeparation *
    process.probeStaMultiplicity * 
    process.staToTkMatchSequenceJPsi *
    process.l1rate *
    process.tpTreeSta
)

## Add extra RECO-level info
if False:
    process.tnpSimpleSequenceSta.replace(process.tpTreeSta, process.tkClusterInfo+process.tpTreeSta)
    process.tpTreeSta.tagVariables.nClustersStrip = cms.InputTag("tkClusterInfo","siStripClusterCount")
    process.tpTreeSta.tagVariables.nClustersPixel = cms.InputTag("tkClusterInfo","siPixelClusterCount")
    process.tnpSimpleSequenceSta.replace(process.tpTreeSta, process.tkLogErrors+process.tpTreeSta)
    process.tpTreeSta.tagVariables.nLogErrFirst = cms.InputTag("tkLogErrors","firstStep")
    process.tpTreeSta.tagVariables.nLogErrPix   = cms.InputTag("tkLogErrors","pixelSteps")
    process.tpTreeSta.tagVariables.nLogErrAny   = cms.InputTag("tkLogErrors","anyStep")

if False: # turn on for tracking efficiency from RECO/AOD + earlyGeneralTracks
    process.tracksNoMuonSeeded = cms.EDFilter("TrackSelector",
      src = cms.InputTag("generalTracks"),
      cut = cms.string(" || ".join("isAlgoInMask('%s')" % a for a in [
                    'initialStep', 'lowPtTripletStep', 'pixelPairStep', 'detachedTripletStep',
                    'mixedTripletStep', 'pixelLessStep', 'tobTecStep', 'jetCoreRegionalStep' ] ) )
    )
    process.pCutTracks0 = process.pCutTracks.clone(src = 'tracksNoMuonSeeded')
    process.tkTracks0 = process.tkTracks.clone(src = 'pCutTracks0')
    process.tkTracksNoJPsi0 = process.tkTracksNoJPsi.clone(src = 'tkTracks0')
    process.tkTracksNoBestJPsi0 = process.tkTracksNoBestJPsi.clone(src = 'tkTracks0')
    process.preTkMatchSequenceJPsi.replace(
            process.tkTracksNoJPsi, process.tkTracksNoJPsi +
            process.tracksNoMuonSeeded + process.pCutTracks0 + process.tkTracks0 + process.tkTracksNoJPsi0 +process.tkTracksNoBestJPsi0
    )
    process.staToTkMatch0 = process.staToTkMatch.clone(matched = 'tkTracks0')
    process.staToTkMatchNoJPsi0 = process.staToTkMatchNoJPsi.clone(matched = 'tkTracksNoJPsi0')
    process.staToTkMatchNoBestJPsi0 = process.staToTkMatchNoBestJPsi.clone(matched = 'tkTracksNoJPsi0')
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatch, process.staToTkMatch + process.staToTkMatch0 )
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatchNoJPsi, process.staToTkMatchNoJPsi + process.staToTkMatchNoJPsi0 )
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatchNoBestJPsi, process.staToTkMatchNoBestJPsi + process.staToTkMatchNoBestJPsi0 )
    process.tpTreeSta.variables.tk0_deltaR     = cms.InputTag("staToTkMatch0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta   = cms.InputTag("staToTkMatch0","deltaEta")
    process.tpTreeSta.variables.tk0_deltaR_NoJPsi   = cms.InputTag("staToTkMatchNoJPsi0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta_NoJPsi = cms.InputTag("staToTkMatchNoJPsi0","deltaEta")
    process.tpTreeSta.variables.tk0_deltaR_NoBestJPsi   = cms.InputTag("staToTkMatchNoBestJPsi0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta_NoBestJPsi = cms.InputTag("staToTkMatchNoBestJPsi0","deltaEta")

process.tagAndProbeSta = cms.Path( 
    process.fastFilter *
    process.HLTMu      *
    process.muonsSta                       *
    process.patMuonsWithTriggerSequenceSta *
    process.tnpSimpleSequenceSta
)


if False: # turn on for tracking efficiency using L1 seeds
    process.probeL1 = cms.EDFilter("CandViewSelector",
        src = cms.InputTag("l1extraParticles"),
        cut = cms.string("pt >= 2 && abs(eta) < 2.4"),
    )
    process.tpPairsTkL1 = process.tpPairs.clone(decay = "tagMuons@+ probeL1@-", cut = 'mass > 5')
    process.l1ToTkMatch    = process.staToTkMatch.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoJPsi = process.staToTkMatchNoJPsi.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoBestJPsi = process.staToTkMatchNoBestJPsi.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatch0    = process.staToTkMatch0.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoJPsi0 = process.staToTkMatchNoJPsi0.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoBestJPsi0 = process.staToTkMatchNoBestJPsi0.clone(src = "probeL1", srcTrack="none")
    process.tpTreeL1 = process.tpTreeSta.clone(
        tagProbePairs = "tpPairsTkL1",
        arbitration   = "OneProbe",
        variables = cms.PSet(
            KinematicVariables,
            bx = cms.string("bx"),
            quality = cms.string("gmtMuonCand.quality"),
            ## track matching variables
            tk_deltaR     = cms.InputTag("l1ToTkMatch","deltaR"),
            tk_deltaEta   = cms.InputTag("l1ToTkMatch","deltaEta"),
            tk_deltaR_NoJPsi   = cms.InputTag("l1ToTkMatchNoJPsi","deltaR"),
            tk_deltaEta_NoJPsi = cms.InputTag("l1ToTkMatchNoJPsi","deltaEta"),
            tk_deltaR_NoBestJPsi   = cms.InputTag("l1ToTkMatchNoBestJPsi","deltaR"),
            tk_deltaEta_NoBestJPsi = cms.InputTag("l1ToTkMatchNoBestJPsi","deltaEta"),
            ## track matching variables (early general tracks)
            tk0_deltaR     = cms.InputTag("l1ToTkMatch0","deltaR"),
            tk0_deltaEta   = cms.InputTag("l1ToTkMatch0","deltaEta"),
            tk0_deltaR_NoJPsi   = cms.InputTag("l1ToTkMatchNoJPsi0","deltaR"),
            tk0_deltaEta_NoJPsi = cms.InputTag("l1ToTkMatchNoJPsi0","deltaEta"),
            tk0_deltaR_NoBestJPsi   = cms.InputTag("l1ToTkMatchNoBestJPsi0","deltaR"),
            tk0_deltaEta_NoBestJPsi = cms.InputTag("l1ToTkMatchNoBestJPsi0","deltaEta"),
        ),
        flags = cms.PSet(
        ),
        tagVariables = cms.PSet(
            pt = cms.string("pt"),
            eta = cms.string("eta"),
            phi = cms.string("phi"),
            nVertices   = cms.InputTag("nverticesModule"),
	    #ERICA:to check if for the JPsi is valid
            #combRelIso = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt"),
            #chargedHadIso04 = cms.string("pfIsolationR04().sumChargedHadronPt"),
            #neutralHadIso04 = cms.string("pfIsolationR04().sumNeutralHadronEt"),
            #photonIso04 = cms.string("pfIsolationR04().sumPhotonEt"),
            #combRelIsoPF04dBeta = IsolationVariables.combRelIsoPF04dBeta,
        ),
        pairVariables = cms.PSet(
            #nJets30 = cms.InputTag("njets30ModuleSta"),
            pt      = cms.string("pt"),
            rapidity = cms.string("rapidity"),
            deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"),
        ),
        pairFlags = cms.PSet(),
        allProbes     = cms.InputTag("probeL1"),
    )
    process.tagAndProbeTkL1 = cms.Path(
        process.fastFilter *
        process.probeL1 *
        process.tpPairsTkL1 *
        process.preTkMatchSequenceJPsi *
        process.l1ToTkMatch * process.l1ToTkMatchNoJPsi * process.l1ToTkMatchNoBestJPsi *
        process.l1ToTkMatch0 * process.l1ToTkMatchNoJPsi0 * process.l1ToTkMatchNoBestJPsi0 *
	#process.nverticesModule * process.l1rate * # added in "add bx information to data tree #18"
        process.tpTreeL1
    )

##    _____     _          ____       _            
##   |  ___|_ _| | _____  |  _ \ __ _| |_ ___  ___ 
##   | |_ / _` | |/ / _ \ | |_) / _` | __/ _ \/ __|
##   |  _| (_| |   <  __/ |  _ < (_| | ||  __/\__ \
##   |_|  \__,_|_|\_\___| |_| \_\__,_|\__\___||___/
##                                                 
##       
#process.load("MuonAnalysis.TagAndProbe.fakerate_all_cff")
#
#process.fakeRateJetPlusProbeTree = process.tpTree.clone(
#    tagProbePairs = 'jetPlusProbe',
#    arbitration   = 'None',
#    tagVariables = process.JetPlusProbeTagVariables,
#    tagFlags = cms.PSet(),
#    pairVariables = cms.PSet(deltaPhi = cms.string("deltaPhi(daughter(0).phi, daughter(1).phi)")),
#    pairFlags     = cms.PSet(),
#    isMC = False, # MC matches not in place for FR yet
#)
#process.fakeRateWPlusProbeTree = process.tpTree.clone(
#    tagProbePairs = 'wPlusProbe',
#    arbitration   = 'None',
#    tagVariables = process.WPlusProbeTagVariables,
#    tagFlags = cms.PSet(),
#    pairVariables = cms.PSet(),
#    pairFlags     = cms.PSet(SameSign = cms.string('daughter(0).daughter(0).charge == daughter(1).charge')),
#    isMC = False, # MC matches not in place for FR yet
#)
#process.fakeRateZPlusProbeTree = process.tpTree.clone(
#    tagProbePairs = 'zPlusProbe',
#    arbitration   = 'None',
#    tagVariables  = process.ZPlusProbeTagVariables,
#    tagFlags      = cms.PSet(),
#    pairVariables = cms.PSet(),
#    pairFlags     = cms.PSet(),
#    isMC = False, # MC matches not in place for FR yet
#)
#
#process.fakeRateJetPlusProbe = cms.Path(
#    process.fastFilter *
#    process.mergedMuons * process.patMuonsWithTriggerSequence *
#    process.tagMuons * process.probeMuons * process.extraProbeVariablesSeq *
#    process.jetPlusProbeSequence *
#    process.fakeRateJetPlusProbeTree
#)
#process.fakeRateWPlusProbe = cms.Path(
#    process.fastFilter *
#    process.mergedMuons * process.patMuonsWithTriggerSequence *
#    process.tagMuons * process.probeMuons * process.extraProbeVariablesSeq *
#    process.wPlusProbeSequence *
#    process.fakeRateWPlusProbeTree
#)
#process.fakeRateZPlusProbe = cms.Path(
#    process.fastFilter *
#    process.mergedMuons * process.patMuonsWithTriggerSequence *
#    process.tagMuons * process.probeMuons * process.extraProbeVariablesSeq *
#    process.zPlusProbeSequence *
#    process.fakeRateZPlusProbeTree
#)

process.schedule = cms.Schedule(
   process.tagAndProbe,
   process.tagAndProbeSta,
   process.tagAndProbeOnePair,
   #process.tagAndProbeTkL1
   #process.fakeRateJetPlusProbe,
   #process.fakeRateWPlusProbe,
   #process.fakeRateZPlusProbe,
)


process.RandomNumberGeneratorService.tkTracksNoJPsi      = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoJPsi0      = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoBestJPsi  = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoBestJPsi0  = cms.PSet( initialSeed = cms.untracked.uint32(81) )

process.TFileService = cms.Service("TFileService", fileName = cms.string("tnpUpsN_Data.root"))   # to avoid mistakes