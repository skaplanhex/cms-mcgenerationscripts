# Auto generated configuration file
# using: 
# Revision: 1.381.2.18 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/SingleElectronPt100_PLTEta_cfi -s GEN,SIM --conditions auto:mc --python_filename=PLTMuonParticleGun_NoSmear_cfg.py --geometry Extended --datatier GEN-SIM --beamspot=NoSmear --eventcontent FEVTDEBUG --no_exec
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')

options.register('outfilename',
                 "MuonGunEvents.root",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "output file name"
                 )
options.register('muonPt',
                    5.,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.float,
                    "muon pT"
                    )
options.register('fullEtaRange',
                    True,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.bool,
                    "run over full eta range"
                    )
options.register('fullPhiRange',
                    True,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.bool,
                    "run over full phi range"
                    )
options.register('sigmaZ',
                    1e-11,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.float,
                    "sigmaZ in "
                    )
options.register('timesPiOverFour',
                    0,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.int,
                    "which telescope")
## 'maxEvents' is already registered by the Framework, changing default value
options.setDefault('maxEvents', 10)

options.parseArguments()
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtendedReco_cff')
process.load('Configuration.Geometry.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
# process.load('Configuration.StandardSequences.VtxSmearedNoSmear_cff')

from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import *
process.GaussVtxSmearingParametersNEW = GaussVtxSmearingParameters.clone(
    SigmaX = 1e-11,
    SigmaY = 1e-11,
    SigmaZ = options.sigmaZ
)
process.VtxSmeared = cms.EDProducer("GaussEvtVtxGenerator",
    process.GaussVtxSmearingParametersNEW,
    VtxSmearedCommon
)



process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
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
    version = cms.untracked.string('$Revision: 1.381.2.18 $'),
    annotation = cms.untracked.string('Configuration/Generator/python/SingleElectronPt100_PLTEta_cfi nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
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

# pt, eta and phi ranges
piOverFour = 3.141592654/4.
fac = options.muonPt*(1e-4)

ptMin = options.muonPt - fac
ptMax = options.muonPt + fac

etaCenter = 4.2373312
phiCenter = 1.9634955

etaMin = etaCenter - (5e-7)
etaMax = etaCenter + (5e-7)

phiMin = phiCenter - (5e-7)
phiMax = phiCenter + (5e-7)

if options.fullEtaRange:
    etaMin = 4.16
    etaMax = 4.32

if options.fullPhiRange:
    # phiMin = 1.8765690
    # phiMax = 2.0504218
    phiMin = 0.0
    phiMax = 2.*3.141592654
process.generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(ptMax),
        MinPt = cms.double(ptMin),
        PartID = cms.vint32(13),
        MaxEta = cms.double(etaMax),
        MaxPhi = cms.double(phiMax+(options.timesPiOverFour*piOverFour)),
        MinEta = cms.double(etaMin),
        MinPhi = cms.double(phiMin+(options.timesPiOverFour*piOverFour))
    ),
    Verbosity = cms.untracked.int32(0),
    psethack = cms.string('single muon pt 50, eta encompasses to PLT'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
)
print "***********************************"
print "* Running muon gun with..."
print "* pT = %1.3f"%options.muonPt
print "* eta min = %1.7f"%etaMin
print "* eta max = %1.7f"%etaMax
print "* phi min = %1.7f"%phiMin
print "* phi max = %1.7f"%phiMax
print "* sigmaZ = %1.2f"%options.sigmaZ
print "***********************************"
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
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 
