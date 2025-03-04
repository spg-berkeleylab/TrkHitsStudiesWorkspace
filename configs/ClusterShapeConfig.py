from Gaudi.Configuration import *
import os

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
from k4FWCore.parseArgs import parser

parser.add_argument(
    "--doTrkDigiSimple",
    help="Only use collections of simplified tracker digitization",
    action="store_true",
    default=False,
)
parser.add_argument(
    "--withClusterFilter",
    help="Use relations collections created after applying cluster filter cuts and renamed without suffix _HTF",
    action="store_true",
    default=False,
)
parser.add_argument(
    "--muColDetGeo",
    help="Muon collider detector geometry, 0-MuCol_v1, 1-MAIA_v0 and 2-MuSIC_v2",
    type=str,
    default=0,
)


the_args = parser.parse_known_args()[0]

if not (the_args.muColDetGeo=="0" or the_args.muColDetGeo=="1" or the_args.muColDetGeo=="2"):
    raise ValueError(f"Invalid detector geometry provided. Acceptable values are 0-MuColv1, 1-MAIAv0 or 2-MuSICv2. Provided value {the_args.muColDetGeo}. Rerun with correct option for --muColDetGeo")


algList = []
evtsvc = EventDataSvc()


CONSTANTS = {
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = WARNING
read.Files = ["output_withbib.slcio"]
algList.append(read)

Config = MarlinProcessorWrapper("Config")
Config.OutputLevel = WARNING
Config.ProcessorType = "CLICRecoConfig"
Config.Parameters = {
                     "Overlay": ["False"],
                     "OverlayChoices": ["False", "BIB"],
                     "Tracking": ["ACTS"],
                     "TrackingChoices": ["Truth", "Conformal", "ACTS"],
                     "VertexUnconstrained": ["OFF"],
                     "VertexUnconstrainedChoices": ["ON", "OFF"]
                     }

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = WARNING
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
                          "HowOften": ["1"]
                          }

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = WARNING
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["histograms_bib_edep"],
                              "FileType": ["root"]
                              }

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = WARNING
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
                         "DD4hepXMLFile": [os.environ.get('MUCOLL_GEO')],
                         "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
                         }

if the_args.muColDetGeo=="1":
    InitDD4hep.Parameters = {"DD4hepXMLFile": ["/global/cfs/projectdirs/atlas/arastogi/MuonCollider/data/MAIA/detector-simulation/geometries/MAIA_v0/MAIA_v0.xml"],
                             "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
                             }
    
if the_args.muColDetGeo=="2":
    InitDD4hep.Parameters = {"DD4hepXMLFile": ["/global/cfs/projectdirs/atlas/arastogi/MuonCollider/code/TrkHitsStudiesWorkspace/packages/lcgeo/MuColl/MuSIC_v2/MuSIC_v2.xml"],
                             "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
                             }

MyTrackTruth = MarlinProcessorWrapper("MyTrackTruth")
MyTrackTruth.OutputLevel = WARNING
MyTrackTruth.ProcessorType = "TrackTruthProc"
MyTrackTruth.Parameters = {
                           "MCParticleCollection": ["MCParticle"],
                           "Particle2TrackRelationName": ["MCParticle_SiTracks"],
                           "TrackCollection": ["SiTracks"],
                           "TrackerHit2SimTrackerHitRelationName": ["VXDBarrelHitsRelations", "ITBarrelHitsRelations", "OTBarrelHitsRelations", "VXDEndcapHitsRelations", "ITEndcapHitsRelations", "OTEndcapHitsRelations"]
                           }

relSuffix = "_HTF"
if the_args.withClusterFilter:
    relSuffix = ""

MyClusterShapeAnalysis = MarlinProcessorWrapper("MyClusterShapeAnalysis")
MyClusterShapeAnalysis.OutputLevel = WARNING
MyClusterShapeAnalysis.ProcessorType = "ClusterShapeHistProc"
MyClusterShapeAnalysis.Parameters = {
                                     "IBRelationCollection": ["ITBarrelHitsRelations"+relSuffix],
                                     "IBTrackerHitsCollection": ["ITBarrelHits"],
                                     "IERelationCollection": ["ITEndcapHitsRelations"+relSuffix],
                                     "IETrackerHitsCollection": ["ITEndcapHits"],
                                     "MCParticleCollection": ["MCParticle"],
                                     "MCTrackRelationCollection": ["MCParticle_SiTracks"],
                                     "OBRelationCollection": ["OTBarrelHitsRelations"+relSuffix],
                                     "OBTrackerHitsCollection": ["OTBarrelHits"],
                                     "OERelationCollection": ["OTEndcapHitsRelations"+relSuffix],
                                     "OETrackerHitsCollection": ["OTEndcapHits"],
                                     "TrackCollection": ["SiTracks"],
                                     "VBRelationCollection": ["VXDBarrelHitsRelations"+relSuffix],
                                     "VBTrackerHitsCollection": ["VXDBarrelHits"],
                                     "VERelationCollection": ["VXDEndcapHitsRelations"+relSuffix],
                                     "VETrackerHitsCollection": ["VXDEndcapHits"],
                                     "muColDet": [the_args.muColDetGeo]
}



algList.append(MyAIDAProcessor)
algList.append(EventNumber)
algList.append(Config)
algList.append(InitDD4hep)

if (the_args.doTrkDigiSimple):
    MyClusterShapeAnalysis.Parameters["IBRelationCollection"]=["ITBarrelHitsRelations"]
    MyClusterShapeAnalysis.Parameters["IERelationCollection"]=["ITEndcapHitsRelations"]
    MyClusterShapeAnalysis.Parameters["OBRelationCollection"]=["OTBarrelHitsRelations"]
    MyClusterShapeAnalysis.Parameters["OERelationCollection"]=["OTEndcapHitsRelations"]
    MyClusterShapeAnalysis.Parameters["VBRelationCollection"]=["VXDBarrelHitsRelations"]
    MyClusterShapeAnalysis.Parameters["VERelationCollection"]=["VXDEndcapHitsRelations"]

algList.append(MyClusterShapeAnalysis)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=WARNING
              )
