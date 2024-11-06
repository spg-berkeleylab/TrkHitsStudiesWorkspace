from Gaudi.Configuration import *
import os

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
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
                                     "OERelationCollection": ["OTEndcapHitsRelations"],
                                     "OTEndcapHitsCollection": ["OTEndcapHits"],
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
algList.append(MyClusterShapeAnalysis)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=WARNING
              )
