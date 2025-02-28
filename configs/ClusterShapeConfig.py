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
muGeo = os.getenv("DET_GEO", 0) #default is MuColv1 geometry
print(f"Detector geometry provided is {muGeo}. Should you need to change, please set the environment variable $DET_GEO as 1 for MAIAv0 or 2 for MuSICv2.")

if not (muGeo=="0" or muGeo=="1" or muGeo=="2"):
    raise ValueError(f"Invalid detector geometry provided. Acceptable values are 0-MuColv1, 1-MAIAv0 or 2-MuSICv2. Provided value {muGeo}.")

the_args = parser.parse_known_args()[0]

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
if muGeo=="1":
    InitDD4hep.Parameters = {"DD4hepXMLFile": ["/global/cfs/projectdirs/atlas/arastogi/MuonCollider/data/MAIA/detector-simulation/geometries/MAIA_v0/MAIA_v0.xml"]}
if muGeo=="2":
    InitDD4hep.Parameters = {"DD4hepXMLFile": ["/global/cfs/projectdirs/atlas/arastogi/MuonCollider/code/TrkHitsStudiesWorkspace/packages/lcgeo/MuColl/MuSIC_v2/MuSIC_v2.xml"]}

MyTrackTruth = MarlinProcessorWrapper("MyTrackTruth")
MyTrackTruth.OutputLevel = WARNING
MyTrackTruth.ProcessorType = "TrackTruthProc"
MyTrackTruth.Parameters = {
                           "MCParticleCollection": ["MCParticle"],
                           "Particle2TrackRelationName": ["MCParticle_SiTracks"],
                           "TrackCollection": ["SiTracks"],
                           "TrackerHit2SimTrackerHitRelationName": ["VXDBarrelHitsRelations", "ITBarrelHitsRelations", "OTBarrelHitsRelations", "VXDEndcapHitsRelations", "ITEndcapHitsRelations", "OTEndcapHitsRelations"]
                           }

MyClusterShapeAnalysis = MarlinProcessorWrapper("MyClusterShapeAnalysis")
MyClusterShapeAnalysis.OutputLevel = WARNING
MyClusterShapeAnalysis.ProcessorType = "ClusterShapeHistProc"
MyClusterShapeAnalysis.Parameters = {
                                     "IBRelationCollection": ["ITBarrelHitsRelations_HTF"],
                                     "IBTrackerHitsCollection": ["ITBarrelHits"],
                                     "IERelationCollection": ["ITEndcapHitsRelations_HTF"],
                                     "IETrackerHitsCollection": ["ITEndcapHits"],
                                     "MCParticleCollection": ["MCParticle"],
                                     "MCTrackRelationCollection": ["MCParticle_SiTracks"],
                                     "OBRelationCollection": ["OTBarrelHitsRelations_HTF"],
                                     "OBTrackerHitsCollection": ["OTBarrelHits"],
                                     "OERelationCollection": ["OTEndcapHitsRelations_HTF"],
                                     "OETrackerHitsCollection": ["OTEndcapHits"],
                                     "TrackCollection": ["SiTracks"],
                                     "VBRelationCollection": ["VXDBarrelHitsRelations_HTF"],
                                     "VBTrackerHitsCollection": ["VXDBarrelHits"],
                                     "VERelationCollection": ["VXDEndcapHitsRelations_HTF"],
                                     "VETrackerHitsCollection": ["VXDEndcapHits"]
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
