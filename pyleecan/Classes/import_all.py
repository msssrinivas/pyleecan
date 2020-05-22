# -*- coding: utf-8 -*-

"""File generated by generate_code() - pyleecan/pyleecan/Generator/run_generate_classes.py
WARNING! All changes made in this file will be lost!
"""

from ..Classes.Arc import Arc
from ..Classes.Arc1 import Arc1
from ..Classes.Arc2 import Arc2
from ..Classes.Arc3 import Arc3
from ..Classes.Bore import Bore
from ..Classes.BoreFlower import BoreFlower
from ..Classes.Circle import Circle
from ..Classes.CondType11 import CondType11
from ..Classes.CondType12 import CondType12
from ..Classes.CondType21 import CondType21
from ..Classes.CondType22 import CondType22
from ..Classes.Conductor import Conductor
from ..Classes.Drive import Drive
from ..Classes.DriveWave import DriveWave
from ..Classes.Electrical import Electrical
from ..Classes.Element import Element
from ..Classes.ElementMat import ElementMat
from ..Classes.Force import Force
from ..Classes.ForceMT import ForceMT
from ..Classes.Frame import Frame
from ..Classes.GUIOption import GUIOption
from ..Classes.Hole import Hole
from ..Classes.HoleM50 import HoleM50
from ..Classes.HoleM51 import HoleM51
from ..Classes.HoleM52 import HoleM52
from ..Classes.HoleM53 import HoleM53
from ..Classes.HoleM54 import HoleM54
from ..Classes.HoleM58 import HoleM58
from ..Classes.HoleMag import HoleMag
from ..Classes.Import import Import
from ..Classes.ImportGenMatrixSin import ImportGenMatrixSin
from ..Classes.ImportGenToothSaw import ImportGenToothSaw
from ..Classes.ImportGenVectLin import ImportGenVectLin
from ..Classes.ImportGenVectSin import ImportGenVectSin
from ..Classes.ImportMatlab import ImportMatlab
from ..Classes.ImportMatrix import ImportMatrix
from ..Classes.ImportMatrixVal import ImportMatrixVal
from ..Classes.ImportMatrixXls import ImportMatrixXls
from ..Classes.Input import Input
from ..Classes.InputCurrent import InputCurrent
from ..Classes.InputCurrentDQ import InputCurrentDQ
from ..Classes.InputFlux import InputFlux
from ..Classes.InputForce import InputForce
from ..Classes.LamHole import LamHole
from ..Classes.LamSlot import LamSlot
from ..Classes.LamSlotMag import LamSlotMag
from ..Classes.LamSlotMulti import LamSlotMulti
from ..Classes.LamSlotWind import LamSlotWind
from ..Classes.LamSquirrelCage import LamSquirrelCage
from ..Classes.Lamination import Lamination
from ..Classes.Line import Line
from ..Classes.Machine import Machine
from ..Classes.MachineAsync import MachineAsync
from ..Classes.MachineDFIM import MachineDFIM
from ..Classes.MachineIPMSM import MachineIPMSM
from ..Classes.MachineSCIM import MachineSCIM
from ..Classes.MachineSIPMSM import MachineSIPMSM
from ..Classes.MachineSRM import MachineSRM
from ..Classes.MachineSyRM import MachineSyRM
from ..Classes.MachineSync import MachineSync
from ..Classes.MachineUD import MachineUD
from ..Classes.MachineWRSM import MachineWRSM
from ..Classes.MagFEMM import MagFEMM
from ..Classes.Magnet import Magnet
from ..Classes.MagnetFlat import MagnetFlat
from ..Classes.MagnetPolar import MagnetPolar
from ..Classes.MagnetType10 import MagnetType10
from ..Classes.MagnetType11 import MagnetType11
from ..Classes.MagnetType12 import MagnetType12
from ..Classes.MagnetType13 import MagnetType13
from ..Classes.MagnetType14 import MagnetType14
from ..Classes.Magnetics import Magnetics
from ..Classes.MatEconomical import MatEconomical
from ..Classes.MatElectrical import MatElectrical
from ..Classes.MatHT import MatHT
from ..Classes.MatMagnetics import MatMagnetics
from ..Classes.MatStructural import MatStructural
from ..Classes.Material import Material
from ..Classes.Mesh import Mesh
from ..Classes.MeshSolution import MeshSolution
from ..Classes.Node import Node
from ..Classes.NodeMat import NodeMat
from ..Classes.Notch import Notch
from ..Classes.NotchEvenDist import NotchEvenDist
from ..Classes.OptiConstraint import OptiConstraint
from ..Classes.OptiDesignVar import OptiDesignVar
from ..Classes.OptiGenAlg import OptiGenAlg
from ..Classes.OptiGenAlgNsga2Deap import OptiGenAlgNsga2Deap
from ..Classes.OptiObjFunc import OptiObjFunc
from ..Classes.OptiProblem import OptiProblem
from ..Classes.OutElec import OutElec
from ..Classes.OutForce import OutForce
from ..Classes.OutGeo import OutGeo
from ..Classes.OutGeoLam import OutGeoLam
from ..Classes.OutMag import OutMag
from ..Classes.OutPost import OutPost
from ..Classes.OutStruct import OutStruct
from ..Classes.Output import Output
from ..Classes.OutputMulti import OutputMulti
from ..Classes.OutputMultiOpti import OutputMultiOpti
from ..Classes.PolarArc import PolarArc
from ..Classes.Segment import Segment
from ..Classes.Shaft import Shaft
from ..Classes.Simu1 import Simu1
from ..Classes.Simulation import Simulation
from ..Classes.Slot import Slot
from ..Classes.Slot19 import Slot19
from ..Classes.SlotMFlat import SlotMFlat
from ..Classes.SlotMPolar import SlotMPolar
from ..Classes.SlotMag import SlotMag
from ..Classes.SlotUD import SlotUD
from ..Classes.SlotW10 import SlotW10
from ..Classes.SlotW11 import SlotW11
from ..Classes.SlotW12 import SlotW12
from ..Classes.SlotW13 import SlotW13
from ..Classes.SlotW14 import SlotW14
from ..Classes.SlotW15 import SlotW15
from ..Classes.SlotW16 import SlotW16
from ..Classes.SlotW21 import SlotW21
from ..Classes.SlotW22 import SlotW22
from ..Classes.SlotW23 import SlotW23
from ..Classes.SlotW24 import SlotW24
from ..Classes.SlotW25 import SlotW25
from ..Classes.SlotW26 import SlotW26
from ..Classes.SlotW27 import SlotW27
from ..Classes.SlotW28 import SlotW28
from ..Classes.SlotW29 import SlotW29
from ..Classes.SlotW60 import SlotW60
from ..Classes.SlotW61 import SlotW61
from ..Classes.SlotWind import SlotWind
from ..Classes.Solution import Solution
from ..Classes.Structural import Structural
from ..Classes.SurfLine import SurfLine
from ..Classes.SurfRing import SurfRing
from ..Classes.Surface import Surface
from ..Classes.Trapeze import Trapeze
from ..Classes.Unit import Unit
from ..Classes.VentilationCirc import VentilationCirc
from ..Classes.VentilationPolar import VentilationPolar
from ..Classes.VentilationTrap import VentilationTrap
from ..Classes.Winding import Winding
from ..Classes.WindingCW1L import WindingCW1L
from ..Classes.WindingCW2LR import WindingCW2LR
from ..Classes.WindingCW2LT import WindingCW2LT
from ..Classes.WindingDW1L import WindingDW1L
from ..Classes.WindingDW2L import WindingDW2L
from ..Classes.WindingSC import WindingSC
from ..Classes.WindingUD import WindingUD
