# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/MinBias_TuneZ2star_14TeV_pythia6_cff -s GEN,SIM --conditions auto:mc --python_filename=minBias_production_pythia6_extgeoPU_14TeV_cfg.py --pileup=2012_Summer_50ns_PoissonOOTPU --geometry Extended --datatier GEN-SIM --eventcontent FEVTDEBUG --no_exec

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')

options.register('outfilename',
                 "outfile14TeVSKIM.root",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "output file name"
                 )
## 'maxEvents' is already registered by the Framework, changing default value
options.setDefault('maxEvents', 2)

options.parseArguments()

import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')

#code from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookSimDigi#ConfigOutput
# process.MessageLogger = cms.Service("MessageLogger",
#     cout = cms.untracked.PSet(
#         default = cms.untracked.PSet(
#             limit = cms.untracked.int32(0) ## kill all messages in the log
#         ),
#         FwkJob = cms.untracked.PSet( 
#             limit = cms.untracked.int32(-1) ## but FwkJob category - those unlimited
#         ),
#         SimG4CoreApplication = cms.untracked.PSet(
#             limit = cms.untracked.int32(-1)
#         )
#     ),
#     categories = cms.untracked.vstring('FwkJob', 'SimG4CoreApplication'),
#     destinations = cms.untracked.vstring('cout')
# )

process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2012_Summer_50ns_PoissonOOTPU_cfi')
process.load('Configuration.Geometry.GeometryExtendedReco_cff')
process.load('Configuration.Geometry.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision1_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.Sim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    annotation = cms.untracked.string('PYTHIA6-MinBias TuneZ2star at 14TeV'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/FourteenTeV/MinBias_TuneZ2star_14TeV_pythia6_cff.py,v $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *',
        'drop *',
        'drop *',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'drop *_g4SimHits_*_*',
        'keep *_g4SimHits_PLTHits_*',
        'keep SimTracks_g4SimHits__*',
        'keep edmHepMCProduct_source_*_*',
        'keep CrossingFramePlaybackInfoExtended_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generator_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep *HaloData_*_*_*',
        'keep *BeamHaloSummary_BeamHaloSummary_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep  *_offlinePrimaryVerticesWithBS_*_*',
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep *_hltL1GtObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep *_genParticle_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep PileupSummaryInfos_*_*_*',) ), 
    fileName = cms.untracked.string(options.outfilename),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(14000.0),
    crossSection = cms.untracked.double(79150000000),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring('MSEL=0         ! User defined processes', 
            'MSUB(11)=1     ! Min bias process', 
            'MSUB(12)=1     ! Min bias process', 
            'MSUB(13)=1     ! Min bias process', 
            'MSUB(28)=1     ! Min bias process', 
            'MSUB(53)=1     ! Min bias process', 
            'MSUB(68)=1     ! Min bias process', 
            'MSUB(92)=1     ! Min bias process, single diffractive', 
            'MSUB(93)=1     ! Min bias process, single diffractive', 
            'MSUB(94)=1     ! Min bias process, double diffractive', 
            'MSUB(95)=1     ! Min bias process'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

