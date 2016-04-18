import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.Configuration.ecalLocalReco_EventContent_cff import *
#
# start with HCAL part
#
#FEVT
RecoLocalCaloFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_hbhereco_*_*', 
                                           'keep *_hbheprereco_*_*',
                                           'keep *_hfreco_*_*', 
                                           'keep *_horeco_*_*',
                                           'keep HBHERecHitsSorted_hbherecoMB_*_*',
                                           'keep HBHERecHitsSorted_hbheprerecoMB_*_*',
                                           'keep HORecHitsSorted_horecoMB_*_*',
                                           'keep HFRecHitsSorted_hfrecoMB_*_*',
                                           'keep ZDCDataFramesSorted_*Digis_*_*',
                                           'keep ZDCRecHitsSorted_*_*_*',
                                           'keep *_reducedHcalRecHits_*_*',
                                           'keep *_castorreco_*_*',
                                           'keep HcalUnpackerReport_*_*_*'
        )
)
#RECO content
RecoLocalCaloRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_hbhereco_*_*',
					   'keep *_hbheprereco_*_*', 
                                           'keep *_hfreco_*_*', 
                                           'keep *_horeco_*_*',
                                           'keep HBHERecHitsSorted_hbherecoMB_*_*',
                                           'keep HORecHitsSorted_horecoMB_*_*',
                                           'keep HFRecHitsSorted_hfrecoMB_*_*',
                                           #'keep ZDCDataFramesSorted_*Digis_*_*',
                                           'keep ZDCDataFramesSorted_hcalDigis_*_*',
                                           'keep ZDCDataFramesSorted_castorDigis_*_*',
                                           'keep ZDCRecHitsSorted_zdcreco_*_*',
                                           'keep *_reducedHcalRecHits_*_*',
                                           'keep *_castorreco_*_*',
                                           #'keep HcalUnpackerReport_*_*_*'
                                           'keep HcalUnpackerReport_castorDigis_*_*',
                                           'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
                                           'keep HcalUnpackerReport_hcalDigis_*_*'
        )
)
#AOD content
RecoLocalCaloAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
    'keep *_castorreco_*_*',
    'keep *_reducedHcalRecHits_*_*',
    #'keep HcalUnpackerReport_*_*_*'
    'keep HcalUnpackerReport_castorDigis_*_*',
    'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
    'keep HcalUnpackerReport_hcalDigis_*_*'
    )
)
RecoLocalCaloFEVT.outputCommands.extend(ecalLocalRecoFEVT.outputCommands)
RecoLocalCaloRECO.outputCommands.extend(ecalLocalRecoRECO.outputCommands)
RecoLocalCaloAOD.outputCommands.extend(ecalLocalRecoAOD.outputCommands)

# mods for HGCAL

_phase2_RecoLocalCaloFEVT_outputCommands = RecoLocalCaloFEVT.outputCommands
_phase2_RecoLocalCaloFEVT_outputCommands.append('keep *_HGCalRecHit_*_*')
_phase2_RecoLocalCaloFEVT_outputCommands.append('keep *_HGCalUncalibRecHit_*_*')

_phase2_RecoLocalCaloRECO_outputCommands = RecoLocalCaloRECO.outputCommands
_phase2_RecoLocalCaloRECO_outputCommands.append('keep *_HGCalRecHit_*_*')

_phase2_RecoLocalCaloAOD_outputCommands = RecoLocalCaloAOD.outputCommands
_phase2_RecoLocalCaloAOD_outputCommands.append('keep *_HGCalRecHit_*_*')

from Configuration.StandardSequences.Eras import eras
eras.phase2_hgcal.toModify( RecoLocalCaloFEVT, outputCommands = _phase2_RecoLocalCaloFEVT_outputCommands )
eras.phase2_hgcal.toModify( RecoLocalCaloRECO, outputCommands = _phase2_RecoLocalCaloRECO_outputCommands )
# don't modify AOD for HGCal yet, need "reduced" rechits collection first (i.e. requires reconstruction)
#eras.phase2_hgcal.toModify( RecoLocalCaloAOD, outputCommands = _phase2_RecoLocalCaloAOD_outputCommands )

